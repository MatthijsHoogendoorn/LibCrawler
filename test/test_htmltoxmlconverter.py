"test_htmltoxmlconverter.py"

import os
import sys

currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from libcrawler.htmltoxmlconverter import convertToXml
from libcrawler.htmlrequesthandler import getHtml

import unittest

class htmlToXmlConverterTests(unittest.TestCase):
    "Test methods for the HtmlToXmlConverter."

    def test_convertToXml(self):
        "Test for convertToXml."

        html = getHtml('https://www.google.com/')
        count1 = len(html)
        xml = convertToXml(html)
        count2 = len(xml)

        self.assertTrue(count1 != count2)

if __name__ == '__main__':
    unittest.main()
