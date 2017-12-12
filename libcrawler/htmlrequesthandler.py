"htmlrequesthandler.py"

import re
import requests
from bs4 import BeautifulSoup

def getHtml(url):
    "Gets html based on url"

    if isValidUrl(url):
        res = requests.get(url)
        html = res.text
        tree = BeautifulSoup(html, "lxml")
        [x.extract() for x in tree.find_all(['script', 'style'])]
        goodhtml = tree.prettify()
        return goodhtml

    return ''



def isValidUrl(url):
    "Checks if the given url is valid"

    result = re.match(r'^(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$', url)
    return result
