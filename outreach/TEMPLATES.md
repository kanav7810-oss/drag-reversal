# Outreach Templates (Handoff Steps 9 + 10)

## How to contact a lab (works for universities and machine shops)

Short email: (a) two-sentence finding summary, (b) the specific question you
cannot answer without them, (c) paper attached, (d) one small concrete ask.
Attach ONE figure (graph2 or graph4), not the whole paper. No open-ended
"will you mentor me".

### Template 1 - university low-speed facility

> Subject: High-school researcher - 2 hours of low-speed tunnel time for a
> riblet validation
>
> Dear Professor [Name],
>
> I am a junior at Rouse High School (Leander, TX). I built a reduced-order
> model from published drag correlations that ranks surface micro-textures
> (riblets, dimples, denticles, hybrids) across two body types and five flow
> speeds; my model predicts blade riblets cut flat-plate friction drag by up
> to 9.5% at s+ = 15 [attach Figure]. The one thing I cannot do alone is a
> clean tripped-flat-plate momentum-deficit measurement at 10-30 m/s.
>
> Would your lab consider two hours of tunnel time - or fifteen minutes of
> advice on rig design - for a student validation campaign? I have coupon
> fabrication underway and a full uncertainty budget written; the manuscript
> is attached.
>
> Thank you either way,
> Kanav Thonda

Targets (handoff Step 9), with the honest caveat: UT Austin's headline aero
tunnels are supersonic/hypersonic. Lead with turbulence-control framing or ask
specifically about teaching tunnels + TACC compute:
- Prof. Noel T. Clemens (UT Austin ASE/EM; Experiments in Fluids EIC 2009-13)
- Flowfield Imaging Lab / Center for Aeromechanics Research admin contacts
- MIT Wright Brothers Wind Tunnel (genuine low-speed facility)
- Georgia Tech Guggenheim School (low-speed/boundary-layer capability)
- Texas A&M Oran W. Nicks Low Speed Wind Tunnel (in-state, runs external
  test campaigns; ask about student/educational slots)
- UT Arlington Aerodynamics Research Center

### Template 2 - compute request (Step 3 LES)

Same skeleton; specific ask: "an allocation of ~5,000 core-hours on a cluster
for a minimal-span riblet LES (OpenFOAM, 1e7 cells)". Mention the smooth-wall
validation gate so they know results will be self-checking.

### Template 3 - fabrication partner (machine shop / makerspace)

> Subject: Student science project - quoting a small aluminium V-groove part
>
> Hi [Shop],
>
> I'm a high-school junior building wind-tunnel test coupons for an aerodynamics
> research project. I need one quote: a 100 mm x 80 mm aluminium 6061 panel with
> V-grooves, pitch 0.5 mm, depth 0.25 mm, over a 90 x 70 mm field (drawing +
> STEP attached). Rough finish is fine inside the grooves; flatness on the back
> face matters more.
>
> Could you quote it at educational cost, or point me to a better process if
> 0.25 mm grooves are outside your wheelhouse? Happy to trade a write-up of
> your shop in my paper's acknowledgements.

Local routes before paying anyone: school makerspace/engineering dept.; Austin
Public Library makerspaces (area labs); UT Austin Texas Inventionworks (check
external-user policy); local machine shops (many quote student work at cost);
photolithography-grade features only via a university cleanroom partnership.

## Follow-up etiquette

One follow-up after 10 business days, then move on. Track in
`outreach/contact_log.csv` (name, org, date sent, response, outcome).
