import os
message_file = 'Domain3/Student/317-message.txt'

# ai. Lines 5-7 check if the message_file exists and removes it and prints a message
if os.path.exists(message_file):
    os.remove(message_file)
    print("Message file removed")

# bi. The else statement on lines 10-11 indiciate if the file doesn't exist
else: 
    print("There was no message file to remove")