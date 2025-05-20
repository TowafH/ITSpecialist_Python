message = open('311-message.txt','w')
message.write('Testing file for player configuration')
message.close()

message_test = open('311-message.txt','r') # r --> Read, default value to open a file and outputs an error if the file doesn't exist
print('311-message is open') 
# Output:
# 311-message.txt will be opened 
