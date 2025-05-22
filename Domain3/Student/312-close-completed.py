# Open for writing purposes
message = open('Domain3/Student/312-message.txt','w')

# Write 2 seperate lines
message.write('Testing file for player configuration') 
message.write('Testing file for player score')

# Close the file
message.close()

# Open the file to read
message_test = open('Domain3/Student/312-message.txt','r')

# Close the file
message_test.close()

