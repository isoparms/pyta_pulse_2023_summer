"""

    Lecture:
        libraries
        import shared.python.x
        build up libraries
        readabiliy vs efficiency vs optimization

    Project 1:
        Shared library 101
        Add list_files() to library
        shared.python.utils
            new fn are_items_in_list()
            new fn empty_list()
            new fn remove_duplicates()
        shared.python.file
            add list_files()
            new fn name()

    Homework:
        1. add new functions to your library
            examples:
                get extension,
                get path,
                does the file exist?
                is it a file or a path?
                copy
                move
                rename

        2. make a PR

"""

import os

# ----------------------------------------------------------------------
# shared.python.utils
# ----------------------------------------------------------------------

def are_items_in_list(items, full_list):
    """

    Will return true if any of the given items are in the given list

    :param items: (list) Items to check against a bigger list.
    :param full_list: (list)
    :return: (bool)

    """
    item_list = make_list(items)

    its = set(item_list)
    fts = set(full_list)

    if len(fts.intersection(its)):
        return True

    return False


def empty_list(number_of_items=0, default_item=None):
    """
    Convenience fn to make a list with a pre-determined number of items.
    Its more readable than:
        var = [None] * number_of_items

    :param number_of_items: (int)
        how many items in the list
    :param default_item:
        the list will come pre filled with that this in every item
        example:
            default_item = "foo"
            return = ["foo", "foo", "foo"...]
    :return:
        (list)
    """

    list_ = [default_item] * number_of_items
    return list_


def remove_duplicates(objects, sort=False):
    if isinstance(objects, list):
        if sort:
            return sorted(list(set(objects)))
        else:
            return list(set(objects))


# ----------------------------------------------------------------------
# shared.python.file
# ----------------------------------------------------------------------
def name(file_path, include_ext=False):
    """
    gets file name without path or extension

    Args:
        file_path:
            (str) file path
        include_ext:
            (bool) have or not have the extension as part of the result

    Returns:
        (str) the name of the file

    """

    file_name = os.path.basename(os.path.splitext(file_path)[0])
    if include_ext:
        return file_name + ext(file_path)

    return file_name
