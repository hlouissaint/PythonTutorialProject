#!/usr/bin/python
import os

p = os.path
try:
    with open("testfile.txt", "a") as fhw:
        fhw.write("This is a test for file exception handling...")
except IOError:
    print("Error: cannot find file or write data...")
    print("Error: cannot find file or write data...")

try:
    with open("testfile.txt", "r") as fhr:
        print(fhr.read())
except IOError :
    print ("Error: cannot find file or read data...")
else:
    print ("File is read successfully...")
    print("File is read successfully...")