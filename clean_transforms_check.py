import maya.cmds as cmds

all_meshes= cmds.select(ado = True)
selected_meshes = cmds.ls(selection = True)
print(selected_meshes)

#variables
mesh_translations = cmds.xform(selected_meshes, ws=True, t=True, q=True)
mesh_rotations = cmds.xform(selected_meshes, ws=True, ro=True, q=True)
mesh_scale = cmds.xform(selected_meshes, ws=True, s=True, q=True)

clean_translations = 0
clean_rotations = 0
clean_scale = 0

for objects in all_meshes:
    for translations in mesh_translations:
        if mesh_translations != 0.0:
            clean_translations = 1
    for rotations in mesh_rotations:
        if mesh_rotations != 0.0:
            clean_rotations = 1
    for scales in mesh_scale:
        if mesh_scale != 1:
            clean_scale = 1
           
            
        
