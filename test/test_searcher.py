"test_searcher.py"

import os
import sys

currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from libcrawler.searcher import Searcher

import unittest


class SearcherTests(unittest.TestCase):
    "Test methods for the Searcher class."

    def test_setUrl(self):
        "Test for setUrl."

        searcher = Searcher()
        urlset = searcher.setUrl('https://www.google.com/')

        self.assertTrue(urlset is True)

    def test_isUrlSet(self):
        "Test for isUrlSet."

        searcher = Searcher()
        searcher.setUrl('https://www.google.com/')

        count = len(searcher.html)
        urlset = (count > 0)
        result = searcher.isUrlSet()

        self.assertTrue(urlset == result)

    def test_searchFor(self):
        "Test for searchFor."

        searcher = Searcher()
        searcher.setUrl('https://travis-ci.org/')

        foundfirst, firsthit = searcher.searchFor('mascot', 1, False, True)
        foundlast, lasthit = searcher.searchFor('Travis', 2, False, False)
        foundall, allhits = searcher.searchFor('Travis', 3, False, False)

        counthits = len(allhits)

        self.assertTrue(foundfirst is True)
        self.assertTrue(foundlast is True)
        self.assertTrue(foundall is True)
        self.assertTrue(firsthit is not None)
        self.assertTrue(lasthit is not None)
        self.assertTrue(allhits is not None)
        self.assertTrue(allhits[counthits - 1] == lasthit)

        foundfirstregex, firstregexhit = searcher.searchFor(r'(?<=Travis )CI - Test', 1, True, False)
        foundlastregex, lastregexhit = searcher.searchFor(r'(?<=get the best Travis )CI', 2, True, False)
        foundallregex, allregexhits = searcher.searchFor(r'(?<=Travis )CI', 3, True, False)

        countregexhits = len(allregexhits)

        self.assertTrue(foundfirstregex is True)
        self.assertTrue(foundlastregex is True)
        self.assertTrue(foundallregex is True)
        self.assertTrue(firstregexhit is not None)
        self.assertTrue(lastregexhit is not None)
        self.assertTrue(allregexhits is not None)
        self.assertTrue(allhits[0] == firstregexhit)
        self.assertTrue(allhits[countregexhits - 1] == lastregexhit)
