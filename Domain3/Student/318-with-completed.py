'''
message = open('Domain3/Student/318-message.txt','w')
message.write('Testing file for player configuration\n')
message.write('Testing file for player score\n')
message.close()
'''

with open('Domain3/Student/318-message.txt', "w") as file:
    file.write('Testing file for player configuration\n')
    file.write('Testing file for player score\n')
    print("File created!")
    # File automatically closes when using a with statement