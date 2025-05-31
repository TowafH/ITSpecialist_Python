score = 200000
level = 3
player1 = "Stacy"

print("Player1:", player1, "Score:", score, "Level:", level)
print("{2} has {0} points and has reached level {1}".format(score, level, player1))
print(f"{player1} has {score} points and has reached level {level}") # Syntax Error w/ incorrect f-string usage
print(f"{player1:<15} {score:>10}") # score:>=10 should be score>:10