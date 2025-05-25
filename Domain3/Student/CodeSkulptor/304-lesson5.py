import sys

# sys.argv[0] --> Always outputs file_name

if len(sys.argv) > 1:
    print('Arguments:', sys.argv[1:])
    # Command in Terminal: python 304-lesson5.py hello 1233 abc
else:
    print("No arguments provided")