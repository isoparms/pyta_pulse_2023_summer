"""

    Lecture:
        context & decorators

    Project 1:
        with selection_restored():

    Project 2:
        @selection_restored_decorator

    Project 3:
        Start file batcher.

    Homework:
        Final project: file batcher

"""

import os

# ----------------------------------------------------------------------
# shared.maya.core.selection
# ----------------------------------------------------------------------
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

