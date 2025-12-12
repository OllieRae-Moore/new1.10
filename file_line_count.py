
# Name: Oliver Rae-Moore
# Username: fwjh0382

import sys

# Show the number of non-empty lines in a text file
# Usage: python file_line_count.py <filename>
# Example: python file_line_count.py textexample.txt
# You must use the error messages precisely as defied below.

# filename is a command line argument 
file_name = ""
# Error message: "Usage: python file_line_count.py <filename.txt>"
if len(sys.argv) != 2:
    raise ValueError(f"Usage: python {sys.argv[0]} <filename.txt>")
file_name = sys.argv[1]
# Open the file and read its content
try:
    with open(file_name,"r") as infile:
        count = 0
        number=0
        for line in infile:
            if line.strip() =="":
                count +=1
                number+= 1
            else:
                number+=1
            

        
except FileNotFoundError:    
    print(f"File not found: {sys.argv[0]} {sys.argv[1]}")

# Error message: "File not found: python file_line_count.py {file_name}"
# count number of lines that are not blank
number_of_lines = 0
number_of_lines = number - count

# success - report the number of lines

# Success message: "{file_name} has {number_of_lines} lines"
print(f"{file_name} has {number_of_lines} lines")

# Test on the 'text_example.txt' file. The answer should be 4.