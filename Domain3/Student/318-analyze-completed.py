#message = open('318-message.txt','w')
#message.write('Testing file for player configuration\n')
#message.write('Testing file for player score\n')
#message.close()

# 2a. The code doesn't work as it's written because print(message.read()) isn't working
with open('Domain3/Student/318-message.text','w+') as message:
    message.write('Testing file for player configuration\n')
    message.write('Testing file for player score\n')
    # message.read() will print now because we utilized .seek(0), which resets the file pointer to the begining. Without it, the file pointer would start at the end of the file.
    message.seek(0)
    print(message.read())
    print('File created')