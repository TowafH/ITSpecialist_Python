message = open('Domain3/Student/314-message.txt','w+') #ci. Indicates that this file can be written 
message.write('Testing file for player configuration\n') # ai. Writes 'Testing file for player configuration' bi. An escape character: '\n'
message.write('Testing file for player score') # ai. Writes 'Testing file for player score'
message.close()

# 2a. False - Python requires code to account for a file that does not exist.
# 2b. True - The r+ and w+ modes of opening a file are the same