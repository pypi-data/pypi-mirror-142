# unit: [length unit:um] [angle unit:degree] [temperature unit:centigrade] [frequency unit:THz]

import matplotlib.pyplot as plt
import seaborn as sns

from maxoptics.sdk import MaxOptics

#########################################
# 1. build structure and set material   #
#########################################

# declare variable object for all project
client = MaxOptics()

# get all waveforms
waveforms = client.search_waveforms()

# create Transition_test.passive project as p
p = client.create_project_as("Transition_test.passive")

# resize halfring_project's w to 100
p.resize(w=100)
p.DOCUMENT.update(w=100, h=100)

# get id of waveform
W1ID = next(filter(lambda _: _["name"] == "Waveform0", waveforms))["id"]

# get id of Si
SiID = client.public_materials["Si (Silicon) - Palik"]["id"]

# get id of SiO2
SiO2ID = client.public_materials["SiO2 (Glass) - Palik"]["id"]

# get id of SiN
SiNID = client.public_materials["Si3N4 (Silicon Nitride) - Kischkat"]["id"]

# set id of Background
BGID = client.user_materials["Air"]["id"]

# add Rectangle to p as waveguide_Si
waveguide_Si = p.add("Rectangle", "waveguide_Si")

# set waveguide_Si's spatial params
waveguide_Si["x"] = -7.5
waveguide_Si["x_span"] = 5
waveguide_Si["y"] = 0
waveguide_Si["y_span"] = 0.5
waveguide_Si["z"] = 0.11
waveguide_Si["z_span"] = 0.22
waveguide_Si["materialId"] = SiID
waveguide_Si["meshOrder"] = 3

# add Rectangle to p as waveguide_SiN
waveguide_SiN = p.add("Rectangle", "waveguide_SiN")

# set waveguide_SiN's spatial params
waveguide_SiN["x"] = 7.5
waveguide_SiN["x_span"] = 5
waveguide_SiN["y"] = 0
waveguide_SiN["y_span"] = 1
waveguide_SiN["z"] = 0.45
waveguide_SiN["z_span"] = 0.3

# set waveguide_SiN's materialId
waveguide_SiN["materialId"] = SiNID

waveguide_SiN["meshOrder"] = 3

# add LinearTrapezoid to p as taper_Si
taper_Si = p.add("LinearTrapezoid", "taper_Si")

# set taper_Si's spatial params
taper_Si["x"] = 0
taper_Si["y"] = 0
taper_Si["z"] = 0.11
taper_Si["z_span"] = 0.22
taper_Si["x0"] = -5
taper_Si["y0"] = 0.25
taper_Si["x1"] = -5
taper_Si["y1"] = -0.25
taper_Si["x2"] = 5
taper_Si["y2"] = -0.04
taper_Si["x3"] = 5
taper_Si["y3"] = 0.04

# set taper_Si's materialId
taper_Si["materialId"] = SiID

taper_Si["meshOrder"] = 3

# add LinearTrapezoid to p as taper_SiN
taper_SiN = p.add("LinearTrapezoid", "taper_SiN")

# set taper_SiN's spatial params
taper_SiN["x"] = 0
taper_SiN["y"] = 0
taper_SiN["z"] = 0.45
taper_SiN["z_span"] = 0.3
taper_SiN["x0"] = -5
taper_SiN["y0"] = 0.25
taper_SiN["x1"] = -5
taper_SiN["y1"] = -0.25
taper_SiN["x2"] = 5
taper_SiN["y2"] = -0.5
taper_SiN["x3"] = 5
taper_SiN["y3"] = 0.5

# set taper_SiN's materialId
taper_SiN["materialId"] = SiNID
taper_SiN["meshOrder"] = 3

# add Rectangle to p as SiO2
SiO2 = p.add("Rectangle", "SiO2")

# set SiO2's spatial params
SiO2["x"] = 0
SiO2["x_span"] = 20
SiO2["y"] = 0
SiO2["y_span"] = 6
SiO2["z"] = 0
SiO2["z_span"] = 6

# set SiO2's materialId
SiO2["materialId"] = SiO2ID

# set SiO2's meshOrder
SiO2["meshOrder"] = 2

#########################################
# 2. set location of source and monitor #
# 3. boundary condition and mesh        #
#########################################

# add FDTD to p as r
r = p.add("FDTD")

# set FDTD's refinement_type [0:Staircase, 1:Dielectric volume average, 2:Average volume average, 3:CP-EP]
r["refinement_type"] = 1

# set r's background_material
r["background_material"] = BGID
# set r's cells_per_wavelength
r["cells_per_wavelength"] = 5

# set r's xyz boundary conditions [0:PML, 1:PEC]
r["x_min_bc"] = 0
r["x_max_bc"] = 0
r["y_min_bc"] = 0
r["y_max_bc"] = 0
r["z_min_bc"] = 0
r["z_max_bc"] = 0
# set r's spatial params
r["x"] = 0
r["x_span"] = 20
r["y"] = 0
r["y_span"] = 5
r["z"] = 0
r["z_span"] = 5

# add ModeSource to p as m
m = p.add("ModeSource")

# set m's injection_axis param [0:x-axis, 1:y-axis ,2:z-axis ]
m["injection_axis"] = 0

# set m's waveform_id
m["waveform_id"] = W1ID

# set m's spatial params
m["x"] = -7
m["y"] = 0
m["y_span"] = 3
m["z"] = 0
m["z_span"] = 3

# add PowerMonitor to p as through
through = p.add("PowerMonitor", "through")
# set through's monitor_type [0:point, 1:linear x, 2:linear y, 3:linear z, 4:2D X-normal, 5:2D Y-normal, 6:2D Z-normal, 7:3D]
through["monitor_type"] = 5

# set through's spatial params
through["x"] = 7
through["y"] = 0
through["y_span"] = 3
through["z"] = 0
through["z_span"] = 3

# add PowerMonitor to p as reflection
reflection = p.add("PowerMonitor", "reflection")
reflection["monitor_type"] = 5

# set reflection's spatial params
reflection["x"] = -8
reflection["y"] = 0
reflection["y_span"] = 3
reflection["z"] = 0
reflection["z_span"] = 3

# add PowerMonitor to p as Y_normal
Y_normal = p.add("PowerMonitor", "Y_normal")

# set Y_normal's monitor_type [0:point, 1:linear x, 2:linear y, 3:linear z, 4:2D X-normal, 5:2D Y-normal, 6:2D Z-normal, 7:3D]
Y_normal["monitor_type"] = 6

# set Y_normal's spatial params
Y_normal["y"] = 0
Y_normal["y_span"] = 0
Y_normal["x"] = 0
Y_normal["x_span"] = 10
Y_normal["z"] = 0
Y_normal["z_span"] = 3

# add GlobalMonitor to p as Y_normal
p.add("GlobalMonitor")

# save project p
p.save()

#########################################
# 4. mode calculation and select source #
# 5. photonics propagation.             #
#########################################

# run t1's FDTD
t1 = p.run("FDTD", async_flag=True)

#########################################
# 6. parameter extraction               #
#########################################

# get t1's intensity data
from maxoptics.plot.heatmap import heatmap

data = t1.passive_fdtd_fd_result_chart("intensity", 0, "E", "ABS", x=0, y="plotX", z="plotY", wavelength=1)

x, y, Z = data.raw_data["horizontal"], data.raw_data["vertical"], data.raw_data["data"]
fig = heatmap(x, y, Z)
plt.savefig("trans_heatmap.jpg")

""" PLEASE USE NEW WAY"""
"""
# draw t1's heatmap
ax = sns.heatmap(
    data=data.DataFrame,
    cmap="jet",
    xticklabels=[round(data.horizontal[0], 2), *([""] * (len(data.horizontal) - 2)), round(data.horizontal[-1], 2)],
    yticklabels=[round(data.vertical[0], 2), *([""] * (len(data.vertical) - 2)), round(data.vertical[-1], 2)],
)
ax.invert_yaxis()
plt.savefig("trans_heatmap.jpg")
"""

plt.clf()

# get t1's line data
data = t1.passive_fdtd_fd_result_chart("line", 0, "T", "ABS", x=0, y=0, z=0, wavelength="plotX")

# draw t1's line map
ax = sns.lineplot(data=data.DataFrame)
plt.savefig("trans_line.jpg")

# transition done msg
print("transition done")
