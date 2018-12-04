#!/usr/bin/python
#
# Solution for Python Challenge #1

import webbrowser

def main():
  baseurl = "http://www.pythonchallenge.com/pc/def/"
  answer = str(2**38)
  webbrowser.open(baseurl+answer+".html")
  
if __name__== "__main__":
  main()

