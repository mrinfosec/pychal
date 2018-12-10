#!/usr/bin/python
#
# Solution for Python Challenge #4

import webbrowser, requests, re

firsturl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=63579"
baseurl = "http://www.pythonchallenge.com/pc/def/"

def gettext(url):
  # pull down the HTML from the link
  r = requests.get(url)
  return r.text

def main():
  i = 0
  url=firsturl
  while i < 400:
    body = gettext(url)
    print(body)
    url=baseurl+"linkedlist.php?nothing="+body.split()[-1]
    i += 1
      
if __name__== "__main__":
  main()

