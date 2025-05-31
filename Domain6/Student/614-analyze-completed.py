import io # Utilized folr in-memory stream

question_stream = io.StringIO() # Creates an in-memory text stream

question_stream.write("The game has started.\n")
question_stream.write("Here is your first question. \n")
question_stream.write("What is the formula for the area of a circle?")

question_stream.seek(0) #  Move the cursor to the beginning
print(question_stream.read()) # Read everything from the beginning