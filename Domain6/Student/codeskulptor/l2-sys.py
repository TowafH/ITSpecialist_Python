import os

os.mkdir("Domain6/Student/codeskulptor/l2-sys-folder")

file_path = "Domain6/Student/codeskulptor/l2-sys-folder/message.txt"

with open(file_path, "w+") as file:
    file.write("I'm created by l2-sys.py!")

    file.seek(0)
    content = file.read()
    print(content)
