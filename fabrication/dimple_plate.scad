// Dimpled flat-plate coupon (B-HEX-* family on the 100 x 80 test panel).
// Units: mm. Hexagonal array of spherical-cap dimples, depth = depth_ratio * d.

plate_w_mm   = 100;
plate_l_mm   = 80;
thickness_mm = 6;
border_mm    = 5;

dimple_d_mm  = 2.0;
depth_ratio  = 0.05;      // B-HEX-d2.0-r0.05
pitch_factor = 1.05;

depth = depth_ratio * dimple_d_mm;
cap_R = (dimple_d_mm*dimple_d_mm/4 + depth*depth) / (2*depth);
ring_r = dimple_d_mm * pitch_factor;

nx = floor((plate_w_mm - 2*border_mm) / ring_r);
ny = floor((plate_l_mm - 2*border_mm) / (ring_r * sin(60)));

difference() {
    cube([plate_w_mm, plate_l_mm, thickness_mm]);
    for (ix = [0 : nx]) {
        for (iy = [0 : ny]) {
            x = border_mm + ix * ring_r + (iy % 2 == 0 ? 0 : ring_r/2);
            y = border_mm + iy * ring_r * sin(60);
            if (x <= plate_w_mm - border_mm && y <= plate_l_mm - border_mm)
                translate([x, y, thickness_mm])
                    cylinder(h = depth*2, r = dimple_d_mm/2, $fn = 48);
        }
    }
    translate([plate_w_mm/2, plate_l_mm/2, 0])
        cylinder(h = thickness_mm, d = 3.2, $fn = 32);
}
echo(str("dimple field: ", nx, " x ", ny, " rings, depth ", depth, " mm"));
