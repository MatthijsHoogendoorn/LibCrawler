from lxml import html, etree
from lxml.etree import tostring


def converttoxml(htmlinput):
    "Converts the given html to xml"
        
    count = len(str(htmlinput))
    if count > 0:
        doc = html.fromstring(htmlinput)
        xml = tostring(doc)
        return xml