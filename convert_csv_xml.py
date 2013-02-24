#!/usr/bin/env python

import datetime
import fileinput
import string
import uuid

def repl_chars(s):
   s = s.replace("&","&amp;")
   s = s.replace("<","&lt;")
   s = s.replace(">","&gt;")
   s = s.replace("\"","&quot;")
   s = s.replace("\'","&apos;")
   return s

print("<!DOCTYPE KEEPASSX_DATABASE>")
print("<database>")
print("<group>")
print("<title>Internet</title>")
print("<icon>1</icon>")

d = datetime.datetime.now()
d = d.replace(microsecond=0)
ds = d.isoformat()
first_line = True
# Iterate through the file a line at a time
for line in fileinput.input():
   if not first_line:
      print("<entry>")
      entries = [ e.strip('"') for e in line.split(',') ]
      print("\t<title>%s</title>" % entries[0])  
      print("\t<username>%s</username>" % entries[1])
      print("\t<password>%s</password>" % repl_chars(entries[2]))
      print("\t<url></url>")  
      print("\t<comment></comment>")
      print("\t<icon>1</icon>")
      print("\t<creation>%s</creation>" % ds) 
      print("\t<lastaccess>%s</lastaccess>" % ds)
      print("\t<lastmod>%s</lastmod>" % ds) 
      print("\t<expire>Never</expire>") 
      print("</entry>")
   else:
      first_line = False

print("</group>")
print("</database>")
