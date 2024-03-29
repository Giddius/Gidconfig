# region [Imports]


# * Standard Library Imports -->
import os
import json

# * Gid Imports -->
import gidlogger as glog

# endregion[Imports]

__updated__ = '2020-11-14 17:08:46'


# region [Logging]

log = glog.aux_logger(__name__)
log.info(glog.imported(__name__))

# endregion[Logging]

# region [Constants]

# endregion[Constants]


def pathmaker(first_segment, *in_path_segments, rev=False):
    """
    Normalizes input path or path fragments, replaces '\\\\' with '/' and combines fragments.

    Parameters
    ----------
    first_segment : str
        first path segment, if it is 'cwd' gets replaced by 'os.getcwd()'
    rev : bool, optional
        If 'True' reverts path back to Windows default, by default None

    Returns
    -------
    str
        New path from segments and normalized.
    """
    _first = os.getcwd() if first_segment == 'cwd' else first_segment
    _path = os.path.join(_first, *in_path_segments)
    _path = _path.replace('\\\\', '/')
    _path = _path.replace('\\', '/')
    if rev is True:
        _path = _path.replace('/', '\\')

    return _path.strip()

# -------------------------------------------------------------- writebin -------------------------------------------------------------- #


def writebin(in_file, in_data):
    # -------------------------------------------------------------- writebin -------------------------------------------------------------- #
    """
    Writes a string to binary.

    Parameters
    ----------
    in_file : str
        The target file path
    in_data : str
        The data to write
    """
    with open(in_file, 'wb') as outbinfile:
        outbinfile.write(in_data)


def writeit(in_file, in_data, append=False, in_encoding='utf-8', in_errors=None):
    """
    Writes to a file.

    Parameters
    ----------
    in_file : str
        The target file path
    in_data : str
        The data to write
    append : bool, optional
        If True appends the data to the file, by default False
    in_encoding : str, optional
        Sets the encoding, by default 'utf-8'
    """
    _write_type = 'w' if append is False else 'a'
    with open(in_file, _write_type, encoding=in_encoding, errors=in_errors,) as _wfile:
        _wfile.write(in_data)


def appendwriteit(in_file, in_data, in_encoding='utf-8'):
    with open(in_file, 'a', encoding=in_encoding) as appendwrite_file:
        appendwrite_file.write(in_data)


def readbin(in_file):
    """
    Reads a binary file.

    Parameters
    ----------
    in_file : str
        A file path

    Returns
    -------
    str
        the decoded file as string
    """
    with open(pathmaker(in_file), 'rb') as binaryfile:
        return binaryfile.read()


def readit(in_file, per_lines=False, in_encoding='utf-8', in_errors=None):
    """
    Reads a file.

    Parameters
    ----------
    in_file : str
        A file path
    per_lines : bool, optional
        If True, returns a list of all lines, by default False
    in_encoding : str, optional
        Sets the encoding, by default 'utf-8'
    in_errors : str, optional
        How to handle encoding errors, either 'strict' or 'ignore', by default 'strict'

    Returns
    -------
    str/list
        the read in file as string or list (if per_lines is True)
    """
    with open(in_file, 'r', encoding=in_encoding, errors=in_errors) as _rfile:
        _content = _rfile.read()
    if per_lines is True:
        _content = _content.splitlines()

    return _content


def linereadit(in_file, in_encoding='utf-8', in_errors='strict'):
    with open(in_file, 'r', encoding=in_encoding, errors=in_errors) as lineread_file:
        _out = lineread_file.read().splitlines()
    return _out


def clearit(in_file):
    """
    Deletes the contents of a file.

    Parameters
    ----------
    in_file : str
        The target file path
    """
    with open(in_file, 'w') as file_to_clear:
        file_to_clear.write('')
    log.debug(f"contents of file '{in_file}' was cleared")


def loadjson(in_file):
    with open(in_file, 'r') as jsonfile:
        _out = json.load(jsonfile)
    return _out


def writejson(in_object, in_file, sort_keys=True, indent=0):
    with open(in_file, 'w') as jsonoutfile:
        json.dump(in_object, jsonoutfile, sort_keys=sort_keys, indent=indent)


# region[Main_Exec]

if __name__ == '__main__':
    pass

# endregion[Main_Exec]
