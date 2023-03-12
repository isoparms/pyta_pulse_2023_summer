"""

    Lecture:
        Maya.
        Install Maya.
        maya.cmds and maya.mel
        Maya commands:
            https://help.autodesk.com/view/MAYAUL/2022/ENU/
            right click menu in script editor

    Project 1:
        Get python running on Maya
        Environment Variables
        userSetup.py
        Maya.env
        C:\Users\<user-name>\OneDrive\Documents\maya\2023

    Project 2:
        shared.maya.core.attribute
        shared.maya.core.node

    Homework:
        1. play in Maya with your library

"""

import os

# ----------------------------------------------------------------------
# shared.maya.core.attribute
# ----------------------------------------------------------------------

def has(attr_path, attr=None):
    """
    Convenience function to be able to type myhi.has(node, attr) rather than cmds.objExists(node + "." + attr)

    :param attr_path: (str) can be a node or an attr path ("node_name" or "node.attr")
    :param attr: (str)
    :return: bool
    """
    if attr:
        attr_path = attr_path + "." + attr
    return cmds.objExists(attr_path)

def ls(node, keyable=False, user_defined=False):
    """
    Convenience func that will return something predictable. Maya's listAttr returns different things.
    :param node: Maya node
    :param keyable: (bool) return only keyable
    :param user_defined:  (bool) return only user defined
    :return:
    """
    res = cmds.listAttr(node, k=keyable, ud=user_defined)
    if not res:
        return []
    else:
        return res



# ----------------------------------------------------------------------
# shared.maya.core.hierarchy
# ----------------------------------------------------------------------
def get_node_type(dag_path, return_shape_type=True):
    """
    Convenience func that will return the shape type as the node type.
    Maya returns the transform type when maya's nodeType is used.

    :param dag_path: (str) Maya DG node
    :param return_shape_type: (bool) return the transform type or the shape type.
    :return:
    """
    dags = pyutils.make_list(dag_path)

    valid_shapes = ["mesh", "nurbsSurface", "nurbsCurve", "locator"]

    ret = list()
    for dag in dags:

        found = False

        if return_shape_type:
            for shape in valid_shapes:
                if has_shape(dag_path, shape_type=shape, true_if_is_shape=True):
                    ret.append(shape.lower())
                    found = True
                    break

        if not found and cmds.objExists(dag):
            ret.append(cmds.nodeType(dag))

    if len(ret) == 1:
        return ret[0]

    return ret


import maya.cmds as cmds


# ----------------------------------------------------------------------
# shared.maya.core.selection
# ----------------------------------------------------------------------
def select_by_type(sel, type="joint"):
    """
    From given list, it will select the items that are of a given node type
    :param sel: (list) list of maya nodes
    :param type: (str) node type
    :return: None
    """
    typed_nodes = list()

    # for multi types, like "constraint"
    # we need multiple strings to check
    if type == "constraint":
        type = [
            "pointConstraint",
            "orientConstraint",
            "aimConstraint",
            "scaleConstraint",
            "parentConstraint"
        ]
    else:
        type = [type]

    for item in sel:
        item_type = cmds.nodeType(item)

        if item_type in type:
            typed_nodes.append(item)

    cmds.select(typed_nodes, replace=True)

# sel = cmds.ls(sl=True)
# select_by_type(sel, type="constraint")
def select_valid(nodes, select=True, replace=True):
    """
    Will check if the nodes exist before trying to select them.
    """
    to_select = list()
    for node in nodes:
        if cmds.objExists(node):
            to_select.append(node)

    if to_select:
        if select:
            cmds.select(to_select, replace=replace)

    return to_select


import contextlib
from functools import wraps
@contextlib.contextmanager
def restore():
    original_selection = cmds.ls(sl=1)
    try:
        yield
    finally:
        cmds.select(cl=1)
        for x in original_selection:
            if cmds.objExists(x):
                cmds.select(x, add=1)


def restore_selection_decorator(func):
    """
    Use as a decorator (@restore_selection_decorator) for maya functions that need to restore seleciton
    """

    @wraps(func)
    def restore_fn(*args, **kwargs):
        original_selection = cmds.ls(sl=1)
        try:
            return func(*args, **kwargs)
        except:
            raise
        finally:
            cmds.select(cl=1)
            for x in original_selection:
                if cmds.objExists(x):
                    cmds.select(x, add=1)

    return restore_fn