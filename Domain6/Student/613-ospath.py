import os.path

if not os.path.exists('Domain6/Student/613-message.txt'):
    message = open('Domain6/Student/613-message.txt','w')
    message.write('Testing file for player configuration\n')
    message.write('Testing file for player score')
    print("Configuration file made")
    message.close()
else: 
    message_test = open('Domain6/Student/613-message.txt','r')
    content = message_test.read()
    print(content)
    message_test.close()

file_path = os.path.join('Domain6/Student/613-test', 'Domain6/Student/613-test.txt')

if os.path.exists(file_path):
    print(f"{file_path}: File Exists!")
else:
    print(f"{file_path} doesn't exist!")