#!/usr/bin/python
#
# Solution for Python Challenge #4

import webbrowser, requests, re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
baseurl = "http://www.pythonchallenge.com/pc/def/"

def gettext(url):
  # pull down the HTML from the link
  r = requests.get(url)
  return r.text

def main():
    

      
if __name__== "__main__":
  main()

