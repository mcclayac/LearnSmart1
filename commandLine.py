import fibonacci as fibonacci

__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/21/16'
__revision__ = '$'
__revision_date__ = '$'


import class5.fibonacci

if __name__ == "__main__":
    import sys
    print("sys.argv[1] : ",  int(sys.argv[1]))

    print(class5.fibonacci.fibolist(int(sys.argv[1])))








