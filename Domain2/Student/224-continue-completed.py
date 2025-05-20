coins = ('Bronze','Silver','Platinum','Gold')
for coin in coins:
    if coin == 'Platinum':
        print('Congratulations! The platinum coin will move you to the next level!')
        continue # The Output: "You possess a Platinum coin." will not run
    print ('You possess a', coin, 'coin.')
    