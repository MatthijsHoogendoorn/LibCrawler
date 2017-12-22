"crawler.py"

import re
from lxml import etree as ET2
from libcrawler.htmltoxmlconverter import convertToXml


class Crawler:
    """Class that serves data by 'crawling' over an xml tree and
    matches the given target with or uses the given regex on the elements."""

    rootnode = None
    xml = ''

    def __init__(self, html):
        self.xml = convertToXml(html)
        self.rootnode = ET2.fromstring(self.xml)

    def getFirstByContentContains(self, target, deepsearch):
        """Search for the given target
        and return the first one found if there is a hit.
        Pass True for deepsearch if attributes also need to be searched."""

        if (target is None) or (len(target) == 0):
            return False, ''

        return self.getFirstRec(target, self.rootnode, False, deepsearch)

    def getFirstByRegex(self, regex, deepsearch):
        """Search with the given regex
        and return the first one found if there is a hit.
        Pass True for deepsearch if attributes also need to be searched."""

        if (regex is None) or (len(regex) == 0):
            return False, ''

        return self.getFirstRec(regex, self.rootnode, True, deepsearch)

    def getFirstRec(self, target, node, isregex, isdeepsearch):
        """Recursively search for the given target in the xml tree
        and return the first hit. Pass True for deepsearch 
        if attributes also need to be searched."""

        if node.text is not None:
            if len(node.text) >= len(target):
                if isregex:
                    match = re.search(target, node.text)
                    if match:
                        return True, node.text
                elif target in node.text:
                    return True, node.text
        elif (node.items() is not None) and (len(node.items())) and isdeepsearch:
            for name, value in node.items():
                if len(value) >= len(target):
                    if isregex:
                        match = re.search(target, value)
                        if match:
                            return True, value
                    elif target in value:
                        return True, value

        if len(node):
            for child in node:
                found, content = self.getFirstRec(
                    target, child, isregex, isdeepsearch)
                if found:
                    return True, content

        return False, ''

    def getLastByContentContains(self, target, deepsearch):
        """Search for the given target and return
        the last one found if there is a hit.
        Pass True for deepsearch if the attributes of elements
        also need to be searched."""

        if (target is None) or (len(target) == 0):
            return False, ''

        hits = self.getAllByRegex(target, deepsearch)
        if (hits is not None) and len(hits):
            return True, hits[len(hits) - 1]

        return False, ''

    def getLastByRegex(self, regex, deepsearch):
        """Search with the given regex and  return
        the last one found if there is a hit.
        Pass True for deepsearch if the attributes of elements
        also need to be searched."""

        if (regex is None) or (len(regex) == 0):
            return False, ''

        hits = self.getAllByRegex(regex, deepsearch)
        if (hits is not None) and len(hits):
            return True, hits[len(hits) - 1]

        return False, ''

    def getAllByContentContains(self, target, deepsearch):
        """Search for the given target and return all
        found hits. Pass True for deepsearch if the attributes of elements
        also need to be searched."""

        hits = []

        if (target is None) or (len(target) == 0):
            return False, hits

        return self.getAllRec(target, self.rootnode, False, deepsearch, hits)

    def getAllByRegex(self, regex, deepsearch):
        """Search with the given regex and return all found hits.
        Pass True for deepsearch if the attributes of elements
        also need to be searched."""

        hits = []

        if (regex is None) or (len(regex) == 0):
            return False, hits

        return self.getAllRec(regex, self.rootnode, True, deepsearch, hits)

    def getAllRec(self, target, node, isregex, isdeepsearch, currentlist):
        """Recursively search for the target in the xml tree
        and return all hits in a list. Pass True for isdeepsearch 
        if attributes also need to be searched."""

        if node.text is not None:
            if len(node.text) >= len(target):
                if isregex:
                    match = re.search(target, node.text)
                    if match:
                        currentlist.append(node.text)
                elif target in node.text:
                    currentlist.append(node.text)
        elif (node.items() is not None) and (len(node.items())) and isdeepsearch:
            for name, value in node.items():
                if value >= target:
                    if isregex:
                        match = re.search(target, value)
                        if match:
                            currentlist.append(value)
                    elif target in value:
                        currentlist.append(value)

        if len(node):
            for child in node:
                self.getAllRec(target, child, isregex,
                               isdeepsearch, currentlist)

        return currentlist
