#!/usr/bin/python3

import cgi
import subprocess as sp

print("content-type: text/html")
print()


a = cgi.FieldStorage()
cmd =a.getvalue("x")

o = sp.getoutput("sudo "+ cmd)
print(o)
