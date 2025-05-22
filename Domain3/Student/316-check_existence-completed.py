import os

# ai. Line 5 checks if 316-message.txt exists. 
# bi. If 316-message.txt doesn't exist, Lines 4-8 will open and create a '316-message.txt' and write text and print a message before closing.                                        
if not os.path.exists('Domain3/Student/316-message.txt'):
    message = open('Domain3/Student/316-message.txt','w')
    message.write('Testing file for player configuration\n')
    message.write('Testing file for player score')
    print("Configuration file made")
    message.close()
# ci. Lines 12-16 would only run if 316-message does exist. They would open the '316-message.txt' in read mode and print the content before closing.
else: 
    message_test = open('Domain3/Student/316-message.txt','r')
    content = message_test.read()
    print(content + "\n")
    print("Configuration file read!")
    message_test.close()