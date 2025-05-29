'''
This code shows items a
player can obtain on each level in a game. Notice that the rock is
not attainable on level 2.
'''

items = ['Wand', 'Rock', 'Pogo Stick']
levels = [1, 2, 3]
for level in levels:
    for item in items:
        if level == 2 and item == 'Rock':
            continue
        else:
            print(f"You can get a {item} at level {level}.")

# 5a. Adding a print statement prints the doc-string at the top in the terminal
print(__doc__)

# 7a.   - Comments cannot span multiple lines, as you would have to use multiple #'s
#       - Docstrings can span multiple lines and called using print(__doc__)
