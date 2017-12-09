"crawler.py"

import re
import xml.etree.ElementTree as ET
from libcrawler.htmltoxmlconverter import converttoxml


class Crawler:
    """Class that serves data by 'crawling' over an xml tree and
    matches the given target with or uses the given regex on the elements."""

    rootnode = None
    xml = ''

    def __init__(self, html):
        self.xml = converttoxml(html)
        self.rootnode = ET.fromstring(self.xml)

    def getFirstByContentContains(self, target):
        """Search for the given target
        and return the first one found if there is a hit."""

        if target is not None:
            count = len(target)
            if count == 0:
                return False, ''

        return self.getFirstRec(target, self.rootnode, False)

    def getFirstByRegex(self, regex):
        """Search with the given regex
        and return the first one found if there is a hit."""

        if regex is not None:
            count = len(regex)
            if count == 0:
                return False, ''

        return self.getFirstRec(regex, self.rootnode, True)

    def getFirstRec(self, target, node, isregex):
        """Recursively search for the given target in the xml tree
        and return the first hit."""

        if node.text is not None:
            if isregex:
                match = re.search(target, node.text)
                if match:
                    return True, node.text
            elif target in node.text:
                return True, node.text

        children = node.getchildren()
        if children is not None:
            count = len(children)
            if count > 0:
                for index in range(0, count):
                    found, content = self.getFirstRec(
                        target, children[index], isregex)
                    if found:
                        return True, content
            else:
                return False, ''

    def getLastByContentContains(self, target):
        """Search for the given target and return
        the last one found if there is a hit."""

        if target is not None:
            count = len(target)
            if count == 0:
                return False, ''

        hits = self.getAllByContentContains(target)
        if hits is not None:
            hitsamount = len(hits)
            if hitsamount > 0:
                return True, hits[hitsamount - 1]

        return False, ''

    def getLastByRegex(self, regex):
        """Search with the given regex and  return
        the last one found if there is a hit."""

        if regex is not None:
            count = len(regex)
            if count == 0:
                return False, ''

        hits = self.getAllByRegex(regex)
        if hits is not None:
            hitsamount = len(hits)
            if hitsamount > 0:
                return True, hits[hitsamount - 1]

        return False, ''

    def getAllByContentContains(self, target):
        """Search for the given target and return all
        found hits."""

        hits = []

        if target is not None:
            count = len(target)
            if count == 0:
                return False, hits

        return self.getAllRec(target, self.rootnode, False, hits)

    def getAllByRegex(self, regex):
        """Search with the given regex and return all found hits."""

        hits = []

        if regex is not None:
            count = len(regex)
            if count == 0:
                return False, hits

        return self.getAllRec(regex, self.rootnode, True, hits)

    def getAllRec(self, target, node, isregex, currentlist):
        """Recursively search for the target in the xml tree
        and return all hits in a list."""

        if node.text is not None:
            if isregex:
                match = re.search(target, node.text)
                if match:
                    currentlist.append(node.text)
            elif target in node.text:
                currentlist.append(node.text)

        children = node.getchildren()
        if children is not None:
            count = len(children)
            if count > 0:
                for index in range(0, count):
                    self.getAllRec(
                        target, children[index], isregex, currentlist)

        return currentlist
