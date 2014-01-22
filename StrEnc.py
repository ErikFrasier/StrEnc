#!/usr/bin/python

import sys,getopt,urllib,HTMLParser,base64,binascii

# Notes:
#

# To do:
#

def usage():
  print 'Usage: '+sys.argv[0]+' -s \"<string to be encoded>\"'

def main(argv):
   encstring = ""
   try:
      opts, args = getopt.getopt(argv,"hs:",["help","string="])
      if not opts:
         print 'No options supplied'
         usage()
         sys.exit(2)
   except getopt.GetoptError:
      usage()
      sys.exit(2)
   for opt, arg in opts:
      if opt in ('-h',"--help"):
         usage()
         sys.exit(2)
      elif opt in ("-s", "--string"):
         encstring = arg
   #original string
   print "================================================================================================================="
   print "Input string to be encoded: \t",encstring
   print "================================================================================================================="
   #URL encoding
   urlenc = urllib.quote_plus(str(encstring.encode("utf-8")))
   print "URL encoding: \t\t\t",urlenc
   doubleurlenc = urllib.quote_plus(str(urlenc))
   print "Double URL encoding:\t \t",doubleurlenc
   #String.fromCharCode
   charcode = ','.join(str(ord(c)) for c in encstring)
   print "String.fromCharCode: \t\t","String.fromCharCode("+charcode+")"
   #HTML encoding
   #
   #BASE64
   base64enc = base64.urlsafe_b64encode(str(encstring.encode("utf-8"))) 
   print "Base64 encoding: \t\t",base64enc
   #Ascii HEX
   asciihexenc = binascii.hexlify(str(encstring.encode("utf-8")))
   print "Ascii Hex encoding: \t\t",asciihexenc
   hexenc = ':'.join(asciihexenc[i:i+2] for i in range(0, len(asciihexenc), 2))
   print "Hex encoding: \t\t\t",hexenc

if __name__ == "__main__":
   main(sys.argv[1:])

