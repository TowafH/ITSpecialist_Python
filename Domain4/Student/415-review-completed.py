'''
This program will run a game, where the user has 3 lives and will reach 
certain positions in each of their lives until they complete the game, which
will output a 'Thank you for playing' message
'''
game_state = True
game_lives = 1
while game_lives <= 3:
    for i in range(1,11):
        print("You have reached position", i, "in game life", game_lives)
    if game_state == True:
        game_lives +=1
print("Thank you for playing.")
print(__doc__)