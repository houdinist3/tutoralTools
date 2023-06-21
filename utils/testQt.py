import os
import maya.standalone
maya.standalone.initialize()
import maya.cmds as cmds


def validateMesh(scene):
    """

        Validate polygon meshes in Maya scene.

        Parameters:
        scene (str): Maya scene with geometry

        Returns:
        validityFlags (str): Str of validation issues

    """
    if os.path.isfile(scene):
        cmds.file(scene, open=True, force=True)

        for obj in cmds.listRelatives(cmds.ls(type='mesh', v=True), p=True, fullPath=True):
            validityFlags = '    scene: %s\n' % scene
            validityFlags += '    mesh: %s\n' % obj

            if not cmds.polyInfo(obj, invalidEdges=True):
                validityFlags += '        invalid edges found\n'
            if not cmds.polyInfo(obj, invalidVertices=True):
                validityFlags += '        invalid vertices found\n'
            if not cmds.polyInfo(obj, laminaFaces=True):
                validityFlags += '        lamina faces found\n'
            if not cmds.polyInfo(obj, nonManifoldEdges=True):
                validityFlags += '        non-manifold faces found\n'
            if not cmds.polyInfo(obj, nonManifoldUVEdges=True):
                validityFlags += '        non-manifold UV edges found\n'
            if not cmds.polyInfo(obj, nonManifoldUVs=True):
                validityFlags += '        non-manifold UVs found\n'
            if not cmds.polyInfo(obj, nonManifoldVertices=True):
                validityFlags += '        non-manifold vertices found\n'

            return validityFlags