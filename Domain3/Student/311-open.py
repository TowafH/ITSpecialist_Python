message = open('Domain3/Student/311-message.txt','w')
message.write('Testing file for player configuration and setup')
message.close() # ci. Closes the file

message_test = open('Domain3/Student/311-message.txt','r') # ai. r --> Read, default value to open a file and outputs an error if the file doesn't exist
print('311-message is open') 
# Output:
# bi. - "311-message is open"
#     - The 311-message.txt file will be opened  

# di. - Parantheses allow for function calls
#     - Grouping mathematical expressions
