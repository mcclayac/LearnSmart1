__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/24/16'
__revision__ = '$'
__revision_date__ = '$'



import os

def standardLibrary1():
    print(os.getcwd())
    os.chdir('/tmp')
    os.system('mkdir temp')

    dir(os)
    # help(os)


def standardLibrary2():
    os.chdir('/tmp')
    import shutil
    shutil.copyfile('data.txt', 'archive.txt')
    #shutil.move('/tmp/test', 'temp')

def standardLibrary3():
    os.chdir('/mcclayac/pythoncode/LearnSmart1/')
    import glob
    print(glob.glob('*.py'))



