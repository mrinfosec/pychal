#!/usr/bin/python
#
# Solution for Python Challenge #2

import webbrowser

def main():
#  crypt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp\
#  i. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.\
#   sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
  baseurl = "http://www.pythonchallenge.com/pc/def/"
  crypt = "map"
  x = "abcdefghijklmnopqrstuvwxyz"
  y = "cdefghijklmnopqrstuvwxyzab"
  map = str.maketrans(x,y)
  answer=crypt.translate(map)
  print(answer)
  webbrowser.open(baseurl+answer+".html")
  
if __name__== "__main__":
  main()

