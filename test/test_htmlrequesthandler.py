import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from libcrawler.htmlrequesthandler import gethtml, isvalidurl

import unittest

class TestMethods(unittest.TestCase):

    def test_isvalidurl(self):
        self.assertTrue(isvalidurl('https://www.google.com/'))
        self.assertTrue(isvalidurl('https://travis-ci.org/'))
        self.assertFalse(isvalidurl('https://travis-ci.!!.org/'))

    def test_gethtml(self):
        html = gethtml('https://travis-ci.org/')
        count = len(html)
        self.assertTrue(count > 0)

if __name__ == '__main__':
    unittest.main()
