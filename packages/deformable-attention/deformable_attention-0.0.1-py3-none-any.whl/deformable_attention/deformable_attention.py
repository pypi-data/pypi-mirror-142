import torch
import torch.nn.functional as F
from torch import nn, einsum

from einops import rearrange, repeat

# helper functions

def exists(val):
    return val is not None

def default(val, d):
    return val if exists(val) else d

def divisible_by(numer, denom):
    return (numer % denom) == 0

class Scale(nn.Module):
    def __init__(self, scale):
        super().__init__()
        self.scale = scale

    def forward(self, x):
        return x * self.scale

# main class

class DeformableAttention(nn.Module):
    def __init__(
        self,
        *,
        dim,
        dim_head = 64,
        heads = 8,
        dropout = 0.,
        downsample_factor = 4,
        offset_scale = 4,
        offset_groups = None,
        offset_kernel_size = 5,
    ):
        super().__init__()
        offset_groups = default(offset_groups, heads)
        assert divisible_by(offset_groups, heads) or divisible_by(heads, offset_groups)

        inner_dim = dim_head * heads
        self.scale = dim_head ** -0.5
        self.heads = heads
        self.offset_groups = offset_groups

        offset_dims = inner_dim // offset_groups

        self.downsample_factor = downsample_factor

        self.to_offsets = nn.Sequential(
            nn.Conv2d(offset_dims, offset_dims, 1, groups = offset_dims, stride = downsample_factor),
            nn.GELU(),
            nn.Conv2d(offset_dims, 2, 1, bias = False),
            nn.Tanh(),
            Scale(offset_scale)
        )

        self.dropout = nn.Dropout(dropout)
        self.to_q = nn.Conv2d(dim, inner_dim, 1, bias = False)
        self.to_kv = nn.Conv2d(dim, inner_dim * 2, 1, bias = False)
        self.to_out = nn.Conv2d(inner_dim, dim, 1)

    def forward(self, x):
        """
        b - batch
        h - heads
        x - height
        y - width
        d - dimension
        g - offset groups
        """

        heads, b, h, w, downsample_factor, device = self.heads, x.shape[0], *x.shape[-2:], self.downsample_factor, x.device

        # queries

        q = self.to_q(x)

        # calculate offsets - offset MLP shared across all groups

        offsets_input = rearrange(q, 'b (g d) ... -> (b g) d ...', g = self.offset_groups)
        offsets = self.to_offsets(offsets_input)

        # calculate grid + offsets

        offsets_h, offsets_w = offsets.shape[-2:]

        grid = torch.stack(torch.meshgrid(
            torch.arange(offsets_h, device = device),
            torch.arange(offsets_w, device = device),
        indexing = 'ij'))

        grid.requires_grad = False
        grid = grid.type_as(x)

        vgrid = grid + offsets

        vgrid_h, vgrid_w = vgrid.unbind(dim = 1)

        vgrid_h = 2.0 * vgrid_h / max(offsets_h - 1, 1) - 1.0
        vgrid_w = 2.0 * vgrid_w / max(offsets_w - 1, 1) - 1.0

        vgrid_scaled = torch.stack((vgrid_h, vgrid_w), dim = -1)

        kv_feats = F.grid_sample(
            offsets_input,
            vgrid_scaled,
        mode = 'bilinear', padding_mode = 'zeros', align_corners = False)

        kv_feats = rearrange(kv_feats, '(b g) d ... -> b (g d) ...', b = b)

        # derive key / values

        k, v = self.to_kv(kv_feats).chunk(2, dim = 1)

        # scale queries

        q = q * self.scale

        # split out heads

        q, k, v = map(lambda t: rearrange(t, 'b (h d) ... -> b h (...) d', h = heads), (q, k, v))

        # query / key similarity

        sim = einsum('b h i d, b h j d -> b h i j', q, k)
        sim = sim - sim.amax(dim = -1, keepdim = True).detach()

        # attention

        attn = sim.softmax(dim = -1)
        attn = self.dropout(attn)

        # aggregate and combine heads

        out = einsum('b h i j, b h j d -> b h i d', attn, v)
        out = rearrange(out, 'b h (x y) d -> b (h d) x y', x = h, y = w)
        return self.to_out(out)
