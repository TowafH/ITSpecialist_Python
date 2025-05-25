with open('Domain3/Student/CodeSkulptor/300-lesson1.txt', 'w') as file:
    file.write("Hello Towaf\n")
    file.write("You're currently in Lesson 1!")

with open('Domain3/Student/CodeSkulptor/300-lesson1.txt', 'r') as file:
    content = file.read()
    print(content)