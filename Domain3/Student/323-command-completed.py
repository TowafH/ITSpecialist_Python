# ai. This program writes in the '323-message.txt' file and writes 2 seperate lines of text and then closes the file and prints a message to indiciate completion.
message = open('Domain3/Student/323-message.txt','w')
message.write('Testing file for player configuration\n')
message.write('Testing file for player score\n')
message.close()
print("Message file complete")

# 4a. False, only on Python 3.6+ --> The f-string feature is available on all versions of Python
# 4b. True, Python must added to the PATH --> One may encounter problems running code from a command line if Python is not set up as an environment variable on their system.