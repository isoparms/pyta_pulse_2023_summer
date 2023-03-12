"""

    Lecture:
        File batcher lecture
        dict()
        json, yml & serialisation of data.

    Project 1:
        Read / Write json data to files.

    Project 2 / Homework:
        File batcher.

"""

import json as _json

def json(path_or_file, obj=None, default=None, indent=4, sort_keys=True):
    """
    Convenient to serialize and deserialize.
    IF you pass a value to arg 'obj', it will be serialized to 'path_or_file'.
    If arg 'obj' is None, the 'path_or_file' will be deserialized and returned.

    Args:
        path_or_file:
            (str or file object)
            Path to the json file on disk
        obj:
            the object to serialize. If not None, the object will be written to
            disk. If it is None, the function will read whats on disk.
        default:
            value to return if file not found or if file is empty.
        indent:
            (int)
             Format spacing for json output
        sort_keys:
            (bool)
            Save with keys sorted.

    Returns:
        None or data - depending on weather obj is set or not

    """

    file_object = None
    path = ""
    if isinstance(path_or_file, IOBase):
        file_object = path_or_file
    else:
        path = os.path.expandvars(path_or_file)

    if not obj is None:

        if path:
            try:
                pyfile.make_dir(os.path.dirname(path))
            except:
                raise Exception("invalid path: \"{0}\"".format(path))

        pylog.info([file_object, path])
        if file_object:
            _json.dump(obj, file_object, indent=indent, sort_keys=sort_keys)
        else:

            with open(path, mode="w") as f:
                _json.dump(obj, f, indent=indent, sort_keys=sort_keys)

        return True

    elif os.path.exists(path) or file_object:
        if file_object:
            # json fails if the file is empty
            try:
                data = _json.load(file_object)
            except ValueError:
                data = default
        else:
            with open(path, mode="r") as f:
                try:
                    data = _json.load(f)
                except ValueError:
                    data = default

        return data

    else:
        return default


def load(path_or_file, default=None, indent=4, sort_keys=True):
    """
    Convenient way to load a JSON file to a dict()

    :param path_or_file: (str or file object) - the path to the json file on disk
    :param default: default: the value to return if file not found or if file is empty
    :param indent: indent: (int) - for formatting json output
    :param sort_keys: sort_keys: (bool) - saved with keys sorted or unsorted.
    :return: (dict) the contents of the file in dict() format.
    """
    return json(path_or_file, obj=None, default=default, indent=indent, sort_keys=sort_keys)


def save(path_or_file, obj, default=None, indent=4, sort_keys=True):
    """
    Convenient way to save a dict() to a JSON file

    :param path_or_file: (str or file object) - the path to the json file on disk
    :param obj: the object to serialize. The object will be written to disk.
    :param default: the value to return if file not found or if file is empty
    :param indent: indent: (int) - for formatting json output
    :param sort_keys: sort_keys: (bool) - saved with keys sorted or unsorted.
    :return: (bool). If file was successfully written or not.
    """
    return json(path_or_file, obj=obj, default=default, indent=indent, sort_keys=sort_keys)
