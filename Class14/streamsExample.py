__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '11/6/16'
__revision__ = '$'
__revision_date__ = '$'



#!/usr/bin/python
def streamExample():
    # import io module
    import io

    print("StringIO : ")
    f = open("myfile.txt", "r", encoding="utf-8")
    f = io.StringIO("some initial text data")
    print("Get Value : ", f.getvalue())
    f.close()

    print("\nBytesIO : ")
    f = open("myfile.jpg", "rb")
    f = io.BytesIO(b"some initial binary data: \x00\x01")
    print("Get Buffer : ", f.getbuffer())
    print("Get Value : ", f.getvalue())
    f.close()

    print("\nUnbufferedIO : ")
    f = open("myfile.jpg", "rb", buffering=0)
    print("Get Value : ", f.readall)
    f.close()


    import time

    print("strftime with gmtime : ",time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()))

    print("strptime : ", time.strptime("30 Nov 00", "%d %b %y"))


def parseArguenents():
    # !/usr/bin/python

    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')

    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()

    print(args.accumulate(args.integers))

def optionalParser():
    # !/usr/bin/python

    from optparse import OptionParser, OptionGroup

    usage = "usage: %prog [options] arg1 arg2"
    parser = OptionParser(usage=usage)
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose", default=True,
                      help="make lots of noise [default]")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose",
                      help="be vewwy quiet (I'm hunting wabbits)")
    parser.add_option("-f", "--filename",
                      metavar="FILE", help="write output to FILE")
    parser.add_option("-m", "--mode",
                      default="intermediate",
                      help="interaction mode: novice, intermediate, "
                           "or expert [default: %default]")

    group = OptionGroup(parser, "Dangerous Options",
                        "Caution: use these options at your own risk.  "
                        "It is believed that some of them bite.")
    group.add_option("-g", action="store_true", help="Group option.")
    parser.add_option_group(group)

    group = OptionGroup(parser, "Debug Options")
    group.add_option("-d", "--debug", action="store_true",
                     help="Print debug information")
    group.add_option("-s", "--sql", action="store_true",
                     help="Print all SQL statements executed")
    group.add_option("-e", action="store_true", help="Print every action done")
    parser.add_option_group(group)

    parser.print_help()
    (options, args) = parser.parse_args()

    print("Options: ", options)
    print("args:", args)


def getOptExample():
    # import getopt module
    import getopt

    args = '-a -b -csample -d example a1 a2'.split()
    print("args : ", args)

    optlist, args = getopt.getopt(args, 'abc:d:')
    print("optlist : ", optlist)

    print("args : ", args)

    s = '--condition=sample --testing --output-file abc.def -x a1 a2'
    args = s.split()
    print("args : ", args)

    optlist, args = getopt.getopt(args, 'x', ['condition=', 'output-file=', 'testing'])
    print("optlist : ", optlist)

    print("args : ", args)


