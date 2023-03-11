"""

    Lecture:
        list()
        bool()
        import
        for
        if

    Project 1:
        list_files(extension='.txt')
        - list()
        - bool()
        - import and use os.path and os.file
        - for:
        - if:

        1. make a fucntion that lists all the files in a folder
        2. only files of a given extension
        3. only files of a given list of extensions
        (stretch)
        4. recursively search files
            - os.walk
            - break
            - continue

    Homework:
        1. finish project
        2. make a PR

"""

import os

def list_files(path, extension=None, recursive=False):
    """
    will return a list of files in a folder.
    By default, it's NOT recursive and will only return the file contents of the base path

    extension can be a list (example: ["ma","mb"])
    return example: ["M:\\file.ma", "M:\\file2.mb"]

    """

    # store the list of files in here:
    all_files = list()
    for (dirpath, dirnames, filenames) in os.walk(path):
        all_files.extend([os.path.join(dirpath, x) for x in filenames])
        if not recursive:
            break

    if extension:

        filtered = list()

        extensions = pyutils.make_list(extension)

        for e in extensions:
            e = "." + e.replace(".", "")

        for i, file_name in enumerate(all_files):
            add = False
            for e in extensions:
                if file_name.endswith(e):
                    add = True
                    break
            if add:
                filtered.append(file_name)

        all_files = filtered

    return all_files