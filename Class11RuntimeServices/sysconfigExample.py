__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/26/16'
__revision__ = '$'
__revision_date__ = '$'


def sysConfig1():
    # !/usr/bin/python

    # import sys module - System-specific parameters and functions.
    import sys

    # displays a list of strings that specifies the search path for modules.
    print("Sys Path : ", sys.path)
    print()

    # displays string contains a platform identifier that can be used to append
    # platform-specific components to sys.path, for instance.
    print("Sys Platform : ", sys.platform)
    print()

    # a tuple containing the five components of the version number
    print("Version Number:  : ", sys.version_info)
    print()

    # the C API version for this interpreter
    print("Sys API Version : ", sys.api_version)
    print()

    # displays a struct sequence giving parameters of the numeric hash implementation.
    print("Sys Hash Info :", sys.hash_info)
    print()

    # returns the name of the encoding used to convert Unicode filenames into system file names.
    print(" Get File System Encoding : ", sys.getfilesystemencoding())
    print()


def sysconfig2():
    # import sysconfig module - Provide access to Pythonâ€™s configuration information
    import sysconfig

    # returns an installation path corresponding to the path name
    print("Path Name : ", sysconfig.get_path("stdlib"))
    print()

    # returns a string that identifies the current platform.
    print("Current Platform : ", sysconfig.get_platform())
    print()

    # returns the MAJOR.MINOR Python version number as a string
    print("Python Version Number : ", sysconfig.get_python_version())
    print()

    # returns a tuple containing all path names
    print("Path Names : ", sysconfig.get_path_names())
    print()

    # returns a tuple containing all schemes
    print("Scheme Names : ", sysconfig.get_scheme_names())
    print()

    # returns the value of a single variable name.
    print("Variable name LIBDIR : ", sysconfig.get_config_var('LIBDIR'))

    # returns the value of a single variable name.
    print("Variable name LIBDEST : ", sysconfig.get_config_var('LIBDEST'))
