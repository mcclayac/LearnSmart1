__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/26/16'
__revision__ = '$'
__revision_date__ = '$'


def contextLib1():
    # import contextlib module - Utilities for with-statement contexts
    from contextlib import closing
    import os

    # import urllib.request module - Extensible library for opening URLs
    from urllib.request import urlopen

    # urlopen returns a bytes object.
    with closing(urlopen('http://www.python.org')) as page:
        for line in page:
            print(line)

    # returns a context manager that suppresses any of the specified exceptions
    from contextlib import suppress

    with suppress(FileNotFoundError):
        os.remove('somefile.tmp')


