from maxoptics import MosLibrary

cl = MosLibrary()
pr = cl.create_project_as("BAP")
pr.add("FDE").update(materialId=cl.public_materials["Si (Silicon)- Palik"]["id"])
pr.save()
pr.run("FDE")
