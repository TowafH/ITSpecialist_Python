game_state = True
game_lives = 1

while game_lives <= 3:
    # Ranges are zero-based
    for i in range(1,11): 
        # Loop to print positions achieved during lives
        print(f"You have reached position {i} in game life {game_lives}")
    if game_state == True:
        game_lives +=1
        # Adding a hashtag symbol to line 10 prevents the games_lives from being incremented
print("Thank you for playing.")

# True, each line of code can have more than on inline comment seperated by #'s