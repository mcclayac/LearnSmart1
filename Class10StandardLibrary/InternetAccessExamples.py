__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/24/16'
__revision__ = '$'
__revision_date__ = '$'


def internetAccess1():
    print("US Naval Observatory Master Clock Time: ")
    from urllib.request import urlopen

    for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
        line = line.decode('utf-8')
        if 'EST' in line or 'EDT' in line:
            print(line)


