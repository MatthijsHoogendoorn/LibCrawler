"htmltoxmlconverter.py"

from lxml import html
from lxml.etree import tostring


def convertToXml(htmlinput):
    "Converts the given html to xml"

    count = len(str(htmlinput))
    if count > 0:
        doc = html.fromstring(htmlinput)
        xml = tostring(doc)
        return xml
