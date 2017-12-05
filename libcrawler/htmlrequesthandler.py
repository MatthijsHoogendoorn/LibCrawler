"htmlrequesthandler.py"

import requests
import re
from bs4 import BeautifulSoup

def gethtml(url):
    "Gets html based on url"

    if isvalidurl(url):
        res = requests.get(url)
        html = res.text
        tree = BeautifulSoup(html, "lxml")
        [x.extract() for x in tree.find_all(['script','style'])]
        goodhtml = tree.prettify()
        return goodhtml

    return ''



def isvalidurl(url):
    "Checks if the given url is valid"

    result = re.match(r'^(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$', url)
    return result
