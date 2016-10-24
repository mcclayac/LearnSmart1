__author__ = 'anthonymcclay'
__project__ = 'LearnSmart1'
__date__ = '10/23/16'
__revision__ = '$'
__revision_date__ = '$'


#!/usr/bin/python

import random
import unittest2



class TestSequenceFunctions(unittest2.TestCase):

    def setUp(self):
        self.seq = list(range(15))

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, list(range(15)))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (7,8,9))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 25)
        for element in random.sample(self.seq, 6):
            self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()
