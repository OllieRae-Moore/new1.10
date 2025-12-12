
# Name: Oliver Rae-Moore
# Username: fwjh0382

# Lists contents of a zip archive
# usage: python ziplist.py <zipfile>
# eg. python ziplist.py testdir/test.zip
# You must use the error messages precisely as defined below.

# Hint: look at the documentation for the "zipfile" module

import sys
import zipfile
#from zipfile import ...   # tools in this module can be used

# filename is a command line argument 
file_name = ""

# Error message: "Usage: python ziplist.py <filename.zip>"
if len(sys.argv) != 2:
    raise ValueError(f"Usage: python {sys.argv[0]} <filename.zip>")
file_name = sys.argv[1]
# Error message: "File not found: python ziplist.py {file_name}"
try:
    with zipfile.ZipFile(file_name,"r") as inzip:
        for file in inzip.namelist():
                print(str(file))
except FileNotFoundError:    
    print(f"File not found: {sys.argv[0]} {sys.argv[1]}")
except zipfile.BadZipFile:
     print(f"Bad zip file: {sys.argv[0]} {file_name}")
     
# Error message: "Bad zip file: python ziplist.py {file_name}"
# Hint: There is an exception for this defined in the zipfile module

# Use zipfile methods to list the contents of the zip file.
# Test your script on the zip_example.zip file. The response should be:
# README.md
# cmd_line.py
# find_file.py
# password.py
# rockpaperscissors.py
