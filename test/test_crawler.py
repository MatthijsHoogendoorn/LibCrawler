"test_crawler.py"

import os
import sys

currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from libcrawler.htmlrequesthandler import getHtml
from libcrawler.crawler import Crawler

import unittest


class CrawlerTests(unittest.TestCase):
    "Test methods for the Crawler class."

    def test_getFirstByContentContains(self):
        "Test method for getFirstByContentContains."

        html = getHtml('https://travis-ci.org/')

        cra = Crawler(html)
        searchcontent = 'mascot'
        found, content = cra.getFirstByContentContains(searchcontent, True)
        self.assertTrue(
            found is True and content is not None and searchcontent in content)

    def test_getFirstByRegex(self):
        "Test method for getFirstByRegex."

        html = getHtml('https://travis-ci.org/')

        cra = Crawler(html)
        regex = r'(?<=Travis )CI'
        found, content = cra.getFirstByRegex(regex, True)
        self.assertTrue(found is True and content is not None)

    def test_getFirstAfter(self):
        "Test method for getFirstAfter."

        html = getHtml('https://travis-ci.org/')

        cra = Crawler(html)
        regex = r'(?<=Travis )CI'
        _, foundtarget = cra.getFirstByRegex(regex, True)
        targetfound, secondtarget = cra.getFirstAfter(regex, foundtarget, True, False)
        self.assertTrue(targetfound is True and secondtarget is not None)

    def test_getFirstBefore(self):
        "Test method for getFirstBefore."

        html = getHtml('https://travis-ci.org/')

        cra = Crawler(html)
        regex = r'(?<=Travis )CI'
        found, foundtarget = cra.getFirstByRegex(regex, True)
        secondtargetfound, secondtarget = cra.getFirstAfter(regex, foundtarget, True, False)
        thirdtargetfound, thirdtarget = cra.getFirstBefore(regex, secondtarget, True, False)

        self.assertTrue(found is True and secondtargetfound is True and thirdtargetfound is True)
        self.assertTrue(thirdtarget == foundtarget)

    def test_getLastByContentContains(self):
        "Test method for getLastByContentContains."

        html = getHtml('https://travis-ci.org/')

        cra = Crawler(html)
        searchcontent = 'Travis'
        expectedcontent = 'Please enable JavaScript to get the best Travis CI experience.'
        found, content = cra.getLastByContentContains(searchcontent, False)
        self.assertTrue(found is True and expectedcontent in content)

    def test_getLastByRegex(self):
        "Test method for getLastByRegex."

        html = getHtml('https://travis-ci.org/')

        cra = Crawler(html)
        regex = r'(?<=Please enable JavaScript to get the best )Travis CI'
        found, content = cra.getLastByRegex(regex, False)
        self.assertTrue(found is True and content is not None)

    def test_getAllByContentContains(self):
        "Test method for getAllByContentContains."

        html = getHtml('https://travis-ci.org/')

        cra = Crawler(html)
        searchcontent = 'Travis'
        hits = cra.getAllByContentContains(searchcontent, False)
        count = len(hits)
        self.assertTrue(count == 3)

    def test_getAllByRegex(self):
        "Test method for getAllByRegex."

        html = getHtml('https://travis-ci.org/')

        cra = Crawler(html)
        regex = r'(?<=Travis )CI'
        hits = cra.getAllByRegex(regex, False)
        count = len(hits)
        self.assertTrue(count == 3)


if __name__ == '__main__':
    unittest.main()
