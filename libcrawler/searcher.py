"searcher.py"

from libcrawler.crawler import Crawler
from libcrawler.htmlrequesthandler import getHtml


class Searcher:
    "This class exposes the API. Use this class to use the library."

    html = ''
    crawler = Crawler

    def setUrl(self, url):
        "This function will get the html representing the given url."

        self.html = getHtml(url)
        if self.isUrlSet():
            self.crawler = Crawler(self.html)
            return True

        return False

    def isUrlSet(self):
        "Checks if the url is set."

        if (self.crawler is not None) and (self.html is not None):
            count = len(self.html)
            if count > 0:
                return True

        return False

    def searchFor(self, data, searchOptions, isRegex, isDeepSearch):
        """Search for data on the web page of the set url.
        Provide a string for data.

        Use the searchOptions as follows:
        1 for returning the first found hit.
        2 for returning the last found hit.
        3 for returning all found hits.

        Provide True for isRegex when the string
        for data is a regular expression.

        Provide True for isDeepSearch if element attributes need to be searched.
        This function will return True/False and any found hit(s)."""

        if (self.isUrlSet()) and (data is not None):
            count = len(data)
            if count > 0:

                if searchOptions == 1:
                    if isRegex:
                        return self.crawler.getFirstByRegex(data, isDeepSearch)
                    else:
                        return self.crawler.getFirstByContentContains(data, isDeepSearch)

                elif searchOptions == 2:
                    if isRegex:
                        return self.crawler.getLastByRegex(data, isDeepSearch)
                    else:
                        return self.crawler.getLastByContentContains(data, isDeepSearch)

                elif searchOptions == 3:
                    if isRegex:
                        listhits = self.crawler.getAllByRegex(data, isDeepSearch)
                        if listhits is not None:
                            count = len(listhits)
                            if count > 0:
                                return True, listhits
                    else:
                        listhits = self.crawler.getAllByContentContains(data, isDeepSearch)
                        if listhits is not None:
                            count = len(listhits)
                            if count > 0:
                                return True, listhits

        return False, None
