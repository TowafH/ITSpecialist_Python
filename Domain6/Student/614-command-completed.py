import sys

filename = sys.argv[1] # Expects an argument to pasesed in the command line.
                       # A 2nd filename must be specified as the 0 index is 614-command.py
                       # Command: python 614-command.py 614-sys.py
print (f" {filename} has been specified.")

with open (filename, 'r') as file:
    content = file.read()
    print(content)

