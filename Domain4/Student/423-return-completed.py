def total_score(score, multiplier):
    return score * multiplier

def welcome():
    print("Welcome to the next level!")

score1 = total_score(3000,2)
score2 = total_score(2000,1.5)

welcome()
print(f"Your two scores are {score1} and {score2}.")

# 1ai. The welcome() message function should store a value for future use to remind the user of their previous scores
# 1bi. The code requires a return statement on line 2 to store the value in the score1 value, which utilizes a function call.
# 2a. Void Function - A function that doesn't return a value after it's executed