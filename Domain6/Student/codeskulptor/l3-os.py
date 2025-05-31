import os

directory = "Domain6/Student/codeskulptor/l3-os-folder"

# Check if directory exists
if not os.path.exists(directory):
    os.makedirs(directory)
    print(f"Directory '{directory}' created.")
else:
    print(f"Directory '{directory}' already exists.")
