from maxoptics.sdk import MaxOptics

#########################################
# 1. build structure and set material   #
#########################################

sdk = MaxOptics()
SiO2 = sdk.public_materials["SiO2 (Glass) - Palik"]["id"]
Si = sdk.public_materials["Si (Silicon)- Palik"]["id"]

project = sdk.create_project_as(name="demo_fde_gds", project_type="passive", log_folder="asdfawwsadf")
project.gds_import(
    "../../../DISTRIBUTION/sdk_demo/imports/gds-example2.GDS", "cell_44", "6/0", "Si (Silicon)- Palik", -0.1, 0.3
)

polygon = project.add_polygon([[-1, 0], [1, 0], [0, 1]])
# polygon["materialId"] = SiO2.iloc[0].at['id']
polygon["materialId"] = SiO2
polygon["z_span"] = polygon["attrs"]["extrude"]["h"] = 4

#########################################
# 2. set location of source and monitor #
# 3. boundary condition and mesh        #
#########################################
fde = project.add("FDE")
fde["background_material"] = SiO2
fde["mesh_cells_x"] = 200
fde["mesh_cells_y"] = 200

# save changed
project.save()
#########################################
# 4. mode calculation and select source #
# 5. photonics propagation.             #
#########################################

simulation_result = project.run(task_type="FDE")

#########################################
# 6. parameter extraction               #
#########################################


# simulation_result.get_mode_solver_result(0, 'Ex', 'Real')


# options = simulation_result.passive_fde_options("intensity", 0)
# data = simulation_result.passive_fde_result_chart("intensity", 0, "E", "ABS^2", x="plotx", y="ploty", z=0,mode=0)


# ax = sns.heatmap(
#     data=data.DataFrame,
#     cmap="jet",
#     xticklabels=[round(data.horizontal[0], 2), *([""] * (len(data.horizontal) - 2)), round(data.horizontal[-1], 2)],
#     yticklabels=[round(data.vertical[0], 2), *([""] * (len(data.vertical) - 2)), round(data.vertical[-1], 2)],
# )

# ax.invert_yaxis()
# plt.savefig("gds_import.jpg")

print("FDE Done")
