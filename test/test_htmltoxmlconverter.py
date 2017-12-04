import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from libcrawler.htmltoxmlconverter import converttoxml
from libcrawler.htmlrequesthandler import gethtml

import unittest

class TestMethods(unittest.TestCase):

    def test_converttoxml(self):

        html = gethtml('https://www.google.com/')
        count1 = len(html)
        xml = converttoxml(html)
        count2 = len(xml)
        print('Length of html = ' + str(count1))
        print('Length of xml = ' + str(count2))

        self.assertTrue(count1 != count2)

if __name__ == '__main__':
    unittest.main()
