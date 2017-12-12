"test_htmlrequesthandler.py"

import os
import sys

currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from libcrawler.htmlrequesthandler import getHtml, isValidUrl

import unittest

class HtmlRequestHandlerTests(unittest.TestCase):
    "Test methods for the HtmlRequestHandler."

    def test_isValidUrl(self):
        "Test for isValidUrl."

        self.assertTrue(isValidUrl('https://www.google.com/'))
        self.assertTrue(isValidUrl('https://travis-ci.org/'))
        self.assertFalse(isValidUrl('https://travis-ci.!!.org/'))

    def test_getHtml(self):
        "Test for getHtml."

        html = getHtml('https://www.google.com/')
        count = len(html)
        self.assertTrue(count > 0)

if __name__ == '__main__':
    unittest.main()
