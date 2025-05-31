import io

game_stream = io.StringIO()

game_stream.write("The game has started.\n")
game_stream.write("Here is your first question. \n")

game_stream.seek(0) # Starts at the begining of the text
print(game_stream.read())

# False --> Bytes IO is a built-in class that only allows in-memory text data storage.

# True --> String IO is a built-in io class that allows users to input text strings into memory and
#retrieve them later.