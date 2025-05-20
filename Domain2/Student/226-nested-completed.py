game_state = True
game_lives = 1
while game_lives <= 3: # Updated the conditional to allow the code to run on the third life
    for i in range(1, 10): # Update the range to start from 1 instead of 0
        print("You have reached position", i, "in game life", game_lives)
    if game_state == True:
        game_lives +=1
print("Thank you for playing.")
