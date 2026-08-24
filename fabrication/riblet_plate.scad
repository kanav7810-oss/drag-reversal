// Parametric riblet test coupon (V-groove or blade cross-section).
// Units: mm. Set s_um/h_um in MICRONS; converted internally.
//
// Examples:
//   A-V-s500-h250   : shape="v", s_um=500, h_um=250
//   A-BLAD-s200-h100: shape="blade", s_um=200, h_um=100
//
// Render with F6 at 0.01 mm resolution before exporting STL.

shape        = "v";          // "v" | "blade"
s_um         = 500;
h_um         = 250;
plate_w_mm   = 100;          // flow direction
plate_l_mm   = 80;           // spanwise (grooves run along this axis)
thickness_mm = 6;
border_mm    = 5;            // plain border around textured field

s = s_um / 1000;
h = h_um / 1000;
n_grooves = floor((plate_l_mm - 2 * border_mm) / s);
field_l   = n_grooves * s;

module v_groove_pair() {
    // one V tooth of base width s, height h, on the plate surface
    translate([0, 0, thickness_mm])
        linear_extrude(height = h)
            polygon(points=[[-s/2, 0], [s/2, 0], [0, h]]);
}

module blade_riblet() {
    // blade: thin fin, tip width ~ min(0.05*s, 0.05*h) with 8 deg draft
    tip_w = min(0.05 * s, 0.05 * h);
    base_w = tip_w + 2 * h * tan(4);
    translate([0, 0, thickness_mm])
        linear_extrude(height = h)
            polygon(points=[[-base_w/2, 0], [base_w/2, 0],
                            [tip_w/2, h], [-tip_w/2, h]]);
}

difference() {
    union() {
        cube([plate_w_mm, plate_l_mm, thickness_mm]);
        for (i = [0 : n_grooves - 1]) {
            y0 = (plate_l_mm - field_l) / 2 + i * s + s/2;
            translate([plate_w_mm/2, y0, 0])
                if (shape == "v") { v_groove_pair(); }
                else { blade_riblet(); }
        }
    }
    // alignment hole for the splitter-plate mounting screw
    translate([plate_w_mm/2, plate_l_mm/2, 0])
        cylinder(h = thickness_mm, d = 3.2, $fn = 32);
}

echo(str("grooves: ", n_grooves, "  pitch: ", s, " mm  height: ", h,
         " mm  textured field: ", plate_w_mm - 2*border_mm, " x ", field_l, " mm"));
