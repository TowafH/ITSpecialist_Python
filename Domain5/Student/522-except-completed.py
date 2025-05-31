figuratives = ['Simile','Metaphor','Personification','Hyperbole','Allusion']

try: # Try will run this code
    figurative_input = int(input('Enter a number from 1-5 to get an example '))
    figurative = figuratives[figurative_input-1]
except: # Except will run IF any error occurs
    print('You did not enter a figurative. Try again')


