#!/usr/bin/python
#
# Solution for Python Challenge #3

import webbrowser, requests

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
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

def histogram(input):
  results = {}
  for char in input:
    if char in results:
      results[char] += 1
    else:
      results[char] = 1
  return results

def main():
  hist = histogram(findcomments(gettext())[1])
  answer = ''
  for letter in hist:
    if hist[letter] < 2:
      answer += letter
  webbrowser.open(baseurl+answer+".html")
      
if __name__== "__main__":
  main()

