#!/usr/bin/python
#
# Solution for Python Challenge #4

import webbrowser, requests, re

url = "http://www.pythonchallenge.com/pc/def/equality.html"
baseurl = "http://www.pythonchallenge.com/pc/def/"

def gettext():
  # pull down the HTML from the link
  r = requests.get(url)
  return r.text

def findcomments(body):
  # returns an array of text strings that 
  # were surrounded by <!-- and -->
  # assumes well-formed comments, won't deal with nested ones
  comments = []
  comment = ""
  arewethereyet = False
  for line in body.splitlines():
    if line == "<!--":
      arewethereyet = True
      continue
    if line == "-->":
      arewethereyet = False
      comments.append(comment)
      comment = ''
    if arewethereyet == True:
      comment += line
  return(comments)

def main():
  answer = ''
  source = findcomments(gettext())[0]
  matches=re.findall(r'[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', source)
  for item in matches:
    answer += item[4]
  webbrowser.open(baseurl+answer+".html")
      
if __name__== "__main__":
  main()

