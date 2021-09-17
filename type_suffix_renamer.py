import maya.cmds as cmds


def rename():
    selection = cmds.ls(selection=True)

    # if nothing is selected, select all visible objects in outliner
    if len(selection) == 0:
        selection = cmds.ls(dag=True, long=True)
    # sort the elements in the list, length wise
    selection.sort(key=len, reverse=True)
    # for the elements in the list, split the name into string where | symbol is
    for obj in selection:
        shortName = obj.split("|")[-1]
        # list the children of the objs if there are any
        children = cmds.listRelatives(obj, children=True, fullPath=True) or []

        # if there are children, show obj type as child
        if len(children) == 1:
            child = children[0]
            objType = cmds.objectType(child)
        # if no child, show parent type
        else:
            objType = cmds.objectType(obj)
            if objType == "mesh":
                suffix = "geo"
            elif objType == "joint":
                suffix = "jnt"
            elif objType == "camera":
                print "Skipping cam"
                continue
            else:
                suffix = "grp"

            if obj.endswith(suffix):
                continue

            newName = shortName + "_" + suffix
            cmds.rename(obj, newName)

    print(selection)
