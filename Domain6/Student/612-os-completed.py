import os

print("Your current directory is:", os.getcwd()) # Print's the current directory

for text_file in os.listdir():
    if text_file.endswith('.txt') and not text_file.startswith('OLD'):
        with open(text_file, 'r') as file:
            content = file.read()
            print(f"--- {text_file} ---")
            print(content)




