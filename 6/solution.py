#!/usr/bin/python
#
# Solution for Python Challenge #6

import webbrowser, requests, pickle

firsturl = "http://www.pythonchallenge.com/pc/def/peak.html"
rawurl = "http://www.pythonchallenge.com/pc/def/banner.p"
baseurl = "http://www.pythonchallenge.com/pc/def/"

def gettext(url):
  # pull down the HTML from the link
  r = requests.get(url)
  return r.text

def main():
  p = pickle.load(open('./banner.p','rb'))
  for line in p:
    for chars in line:
      print(chars[0]*chars[1], end='')
    print()
      
if __name__== "__main__":
  main()

