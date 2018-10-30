'''
Maya Intrinsic Imports
'''
import maya.cmds as mc
import maya.api.OpenMaya as om
import pymel.core as pm

def fetch_selection(OpenMaya=False, cmds = False, pymel=False, shape=False):
    if OpenMaya:
        sel_list = om.MGlobal.getActiveSelectionList()
        path = sel_list.getDagPath(0)
        path.extendToShape()
        surface = om.MFnMesh(path)
        return surface
    elif cmds:
        selection = mc.ls(selection=1, l=1)[0]
        return selection
    elif shape:
        selection = mc.ls(selection=1, l=1)[0]
        selection = mc.listRelatives(selection, shapes=1, ad=1, f=1)[0]
        return selection
    elif pymel:
        return
    else:
        print "No Method of Selection chosen, valid args:\n" \
              " <OpenMaya>, <cmds>, <pymel>, <shape> "



