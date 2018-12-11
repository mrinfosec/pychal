#!/usr/bin/python
#
# Solution for Python Challenge #7

import webbrowser, requests, zipfile

firsturl = "http://www.pythonchallenge.com/pc/def/channel.html"
seed = '90052'

def gettext(url):
  # pull down the HTML from the link
  r = requests.get(url)
  return r.text

def main():
  current = seed
  zip = zipfile.ZipFile('channel.zip', 'r')
  comments=''

  for i in range(1000):
    filename = current + '.txt'
    comments += zip.getinfo(filename).comment.decode('UTF-8')
    f = open(filename,'r')
    line = f.read()
    print(line)
    current = line.split()[-1]
    print(comments)

if __name__== "__main__":
  main()

