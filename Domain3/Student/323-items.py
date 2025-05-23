level = int(input("Enter the desired level: "))
level_1_items = ("Rock", "Pogo Stick")
level_2_items = ("Wand", "Pogo Stick")
level_3_items = ("Wand", "Rock", "Pogo Stick")


def game(level):
    if level == 1:
        for item in level_1_items:
            print(f"You can get a {item} at level {level}")
    elif level == 2:
        for item in level_2_items:
            print(f"You can get a {item} at level {level}")
    elif level == 3:
        for item in level_3_items:
            print(f"You can get a {item} at level {level}")
    else:
        level = int(input("Enter a level between 1 and 3: "))
        game(level)

game(level)
