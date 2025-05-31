coins = 5
games = 2
try:
    result = coins/games
except:
    print('This did not work. Did you to divide by zero?') # This will run when games = 0
else:
    print('You are averaging', coins/games, 'coins per game.') # This will run when games = 2
finally:
    print('Thank you for playing') # This will run games = 0 | This will run when games = 2