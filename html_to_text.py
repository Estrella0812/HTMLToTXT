#This will not run on online IDE
import requests
import js2py
from bs4 import BeautifulSoup

URL = "https://www.minimallstorage.com/self-storage/new-brunswick/nauwigewauk/298-route-100/"
r = requests.get(URL)

# soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib


response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
text = soup.prettify()


with open('raw_html.txt', 'w', encoding='utf-8') as f:
    f.write(text)


dontWrite = False
lines = []
# read file
with open('raw_html.txt', 'r', encoding='utf-8') as fp:
    # read an store all lines into list
    lines = fp.readlines()


# Get rid of header
with open('raw_html.txt', 'w', encoding='utf-8') as fp:
    # iterate each line
    for number, line in enumerate(lines):
        # delete line 5 and 8. or pass any Nth line you want to remove
        # note list index starts from 0
        if line.strip().startswith("<head>"):
            dontWrite = True
        if dontWrite == False:
           fp.write(line)
        if line.strip().startswith("</head>"):
            dontWrite = False






# eval_res, jsFile = js2py.run_file('cleanText.js')
# jsFile.convertToText()

# eval_res, tempfile = js2py.run_file("html_clean_txt.js")
# tempfile.convertToText()