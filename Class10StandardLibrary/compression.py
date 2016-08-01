__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '7/26/16'
__revision__ = '$'
__revision_date__ = '$'


def zlibCompression():
    import zlib
    s = b'For appications that require data compressionm the function in this module allow compression and decompression using the zlib library'
    print('String :', s)
    print('Length: ', len(s))

    t = zlib.compress(s)
    print('length after compression: ', len(t))
    print('String after decompress: ',  zlib.decompress(t))
    print('Using crc32: ', zlib.crc32(s))
    print ('---------------------------------\n\n')





def timeitExample():
    # import timeit module
    from timeit import Timer

    print("performance of Timer('temp=a; a=b; b=temp', 'a=1; b=2'): ",
          Timer('temp=a; a=b; b=temp', 'a=1; b=2').timeit())
    print("performance of Timer('a,b = b,a', 'a=1; b=2'): ", Timer('a,b = b,a', 'a=1; b=2').timeit())

    print("------------------------------------------")

def average(values):
   return sum(values) / len(values)


# import unittest module
import unittest
import math

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([40, 60, 140]), 80.0)
        self.assertEqual(round(average([2, 3, 8]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(40, 60, 140)
#  invokes all tests
unittest.main()
