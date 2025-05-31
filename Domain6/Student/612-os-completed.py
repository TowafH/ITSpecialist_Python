import os

print("Your current directory is:", os.getcwd()) # Print's the current directory

if "612-os.txt" in os.listdir():
    os.rename("612-os.txt", "OLD612-os.txt")
    print("Renamed 601-message.txt to OLD601-message.txt")

for text_file in os.listdir():  # os.listdir lists all files and folders in the current working directory.
    if text_file.endswith('.txt'):
        with open(text_file, 'r') as file:
            content = file.read()
            print(f"--- {text_file} ---")
            print(content)




