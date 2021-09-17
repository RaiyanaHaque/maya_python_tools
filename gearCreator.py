from maya import cmds


def create_gear(teeth=10, length=0.3):
    """
    This function will create a gear with the given parameters

    :param teeth: The number of teeth to create
    :param length: The length of the teeth
    :return:
        A tuple of the transform, constructor and extrude node

    """
    spans = teeth * 2

    transform, constructor = cmds.polyPipe(subdivisionsAxis=spans)

    # selects the faces within the range given, chooses every other face
    side_faces = range(spans * 2, spans * 3, 2)

    cmds.select(clear=True)

    # %s will take on the words in the brackets in the respective order, add it each time
    for face in side_faces:
        cmds.select('%s.f[%s]' % (transform, face), add=True)

    extrude = cmds.polyExtrudeFacet(localTranslateZ=length)[0]
    return transform, constructor, extrude


def change_teeth(constructor, extrude, teeth=10, length=0.3):
    """
       Change the number of teeth on a gear with a given number of teeth and a given length for the teeth.
       This will create a new extrude node.
       Args:
           constructor (str): the constructor node
           extrude (str): the extrude node
           teeth (int): the number of teeth to create
           length (float): the length of the teeth to create
       """

    spans = teeth * 2

    # the edit flag will make sure not to create a new one, and change the teeth for the existing one
    cmds.polyPipe(constructor, edit=True, subdivisionsAxis=spans)

    side_faces = range(spans*2, spans*3, 2)
    face_names = []

    for face in side_faces:
        face_names = 'f[%s]' % face
        face_names.append(face_names)

    cmds.setAttr('%s.inputComponents' % extrude, len(face_names), *face_names, type="componentList")
    cmds.polyExtrudeFacet(extrude, edit=True, ltz=length)