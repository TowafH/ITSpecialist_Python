import os
import datetime

x = datetime.datetime.now()

if os.path.exists('Domain3/Student/CodeSkulptor/301-lesson2.txt'):
    print("File Exists!")
    os.remove('Domain3/Student/CodeSkulptor/301-lesson2.txt')
else:
    with open('Domain3/Student/CodeSkulptor/301-lesson2.txt', "w+") as file:
        file.write(f"{x.strftime("%b %m %Y")}")
        content = file.read()
        print(content)