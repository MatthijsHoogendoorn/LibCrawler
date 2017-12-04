"htmlrequesthandler.py"

import urllib.request
import re
from bs4 import BeautifulSoup

def gethtml(url):
    "Gets html based on url"

    if isvalidurl(url):

        with urllib.request.urlopen(url) as response:
            html = response.read()
            tree = BeautifulSoup(html, "html.parser")
            goodhtml = tree.prettify()
            return goodhtml

def isvalidurl(url):
    "Checks if the given url is valid"

    result = re.match(r'^(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$', url)
    return result
