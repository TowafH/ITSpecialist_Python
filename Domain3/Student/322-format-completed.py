score = 200000
level = 3
player1 = "Stacey"

print("Player1:", player1, "Score:", score, "Level:", level)

print("{2} has {0} points and has reached level {1}".format(score, level, player1)) 
# 1ai. The .format() method is used to insert variables into the string using placeholder brackets.
# 1bi. The numbers in brackets refer to the index positions of the arguments passed into the .format() method.
#      For example, {0} refers to score, which is the first argument, so score == argument 0.

print(f"{player1} has {score} points and has reached level {level}") 
# 1ci. f-strings are used to embed variables directly into a string by placing them inside curly braces {}.

# 2a. f-strings are the preferred method of formatting strings in Python 3.6 because it is easier to read and faster
# 3a. The modulos operator (%) mimics the behavior of remainder divison