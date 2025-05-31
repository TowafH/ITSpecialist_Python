figuratives = ['Simile','Metaphor','Personification','Hyperbole','Allusion']
try: # Run the Code
    figurative_input = int(input('Enter a number from 1-5 to get an example '))
    figurative = figuratives[figurative_input-1]
except: # Executes if an error occurs
    print('You did not enter a figurative. Try again')
else: # Executes of try doesn't raise an error
    print(f'You chose the {figurative} figurative and will get an example soon.')
finally: # Will Always run regardless
    print("Thank you for playing!")