coins = ['Bronze', 'Silver', 'Gold','Platinum']
coin = 'gold' # a. The value of the coin variable is lowercase, when it should be uppercause
score = 10000

if score > 10000: # b. The conditional statement should be >= because when the player reaches 10,000 points they should level up.
    if coin in ('Gold','Platinum'):
        print("You have reached level 3") # Expected Output
    else:
        print("You have reached level 2")
elif score > 5000 and coin in coins:
    print("You have reached level 1. Keep going")
else:
    print("Increase your score and collect coins to move up") # Problem Output