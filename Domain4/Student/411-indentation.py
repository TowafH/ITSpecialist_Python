game_state = True
game_lives = 1
while game_lives <= 3:
    for i in range(1,11):
        print("You have reached position", i, "in game life", game_lives)
    if game_state == True:
        game_lives +=1
    print("Thank you for playing.") # 1ai. This line will run once when the program completes iterating through the While statement
                                    # 1bi. Indenting line 8 to be within the While loop will repeat it with every iteration
                                    # 2a. 4 Spaces or 1 indentation is necessary
                                    # 3a. False, not all editors will immediantly provide a tooltip telling users when their indentation is inconsistent.
                                    # 4a. It's important to be consistent with indentation to avoid errors, make the code easier to document, and improve collaboration
                                    # 5a. Python3 doesn't allow mixing tabs and spaces in a single block of code because it helps prevent ambiguous and hard-to-detect indentation errors.
                                    