// Dimpled sphere, 42.7 mm (golf-ball scale) - hex-packed spherical-cap dimples.
// Units: mm.
//
// B-HEX-d2.0-r0.1  -> dimple_d_mm=2.0, depth_ratio=0.10
// E-SMOOTH         -> dimple_d_mm=0 (renders plain sphere)

D_mm          = 42.70;
dimple_d_mm   = 2.0;
depth_ratio   = 0.10;     // dimple depth / dimple diameter
pitch_factor  = 1.05;     // hex pitch = pitch_factor * d (tunes coverage)
fill_hole_d   = 3.0;

depth = depth_ratio * dimple_d_mm;
cap_R = (dimple_d_mm*dimple_d_mm/4 + depth*depth) / (2*depth); // cap radius

module dimple_at(p) {
    // place a spherical-cap cutter tangent to the sphere surface at point p
    n = p / norm(p);
    translate(n * (D_mm/2 - depth + cap_R))
        sphere(r = cap_R, $fn = 48);
}

difference() {
    sphere(d = D_mm, $fn = 160);
    if (dimple_d_mm > 0) {
        ring_r = dimple_d_mm * pitch_factor;
        for (ring = [0 : 8]) {
            rr = ring * ring_r * sin(60);
            count = max(1, floor(2 * 3.14159 * max(rr, 0.001) / (ring_r * 2)) );
            offset = ring % 2 == 0 ? 0 : 180 / count;
            for (k = [0 : count-1]) {
                ang = k * 360 / count + offset;
                x = rr * cos(ang);
                y = rr * sin(ang);
                z_sq = D_mm*D_mm/4 - rr*rr;
                if (z_sq > (ring_r*0.6)^2) {
                    dimple_at([x, y, sqrt(z_sq)]);
                }
            }
        }
    }
    // ballast filling hole at pole; seal with matching plug after mass trim
    rotate([90, 0, 0])
        cylinder(h = 6, d = fill_hole_d, $fn = 32, center = false);
}
echo(str("dimple depth: ", depth, " mm, cap R: ", cap_R, " mm"));
