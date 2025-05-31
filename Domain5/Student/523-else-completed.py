figuratives = ['Simile','Metaphor','Personification','Hyperbole','Allusion']
try: # Run the code
    figurative_input = int(input('Enter a number from 1-5 to get an example '))
    figurative = figuratives[figurative_input-1]
except: # Execute if error occurs
    print('You did not enter a figurative. Try again')
else: # Executes if try does not raise an error
    print(f'You chose the {figurative} figurative and will get an example soon.')
