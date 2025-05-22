# Seperate Code
message = open('Domain3/Student/313-message.txt','w')
message.write('Testing file for player configuration\n')
message.write('Testing file for player score')
message.close()

# Seperate Code
message_test = open('Domain3/Student/313-message.txt','r+')

content = message_test.read() # Allow for the reading of the content
print(content) # Print text within the file

message_test.close()

# 5a. 'r+ mode' in Python provides the ability to both read and write to a file.
# 6a. It is necessary to look through the file's content through a print statement to view its contents and consider its usecase
