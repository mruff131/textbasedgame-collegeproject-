# Mariah Ruff's Text Based Game

# create a function to display instructions to user
def display_instructions():
    print('Welcome to Spider Escape Game')
    print('You are trapped inside an abandoned building and must escape!')
    print('You must collect the 6 hidden items to defeat the MEGA SPIDER!')
    print('If you run into the MegaSpider before collecting all the items, you lose!')
    print('Hurry! The building contains thousands of unhatched Mega Spider eggs.')
    print('If you dont blow up the building in time, you lose!')
    print('---------------------------------------------------------------------------')
    print('Enter "ok" to continue.')


# create a function for player commands
def player_commands():
    print('---------------------------------------------------------------------------')
    print('Move commands: go North, go South, go East, go West')
    print('To grab an item, type "grab item"')
    print('To walk past an item, type "pass"')
    print('To UNLOCK treasure chest, type "unlock item"')
    print('To kill the mega spider, type "shoot spider"')
    print('To throw the grenade, type "throw grenade"')
    print('For instructions, enter "need help"  anytime')


display_instructions()

while True:
    user_input = input()
    user_input = user_input.lower()
    if user_input == 'ok':
        player_commands()  # call the player instructions from above
        break
    else:
        print('Invalid entry, enter "ok" to continue')
        user_input = input(str())


# created a main function for game
def main():
    current_room = 'Waiting Room'
    player_inventory = []
    global number_of_lives  # declare variable global so I can alter number of lives inside function
    number_of_lives = 1

    complete_inventory = {'night vision goggles', 'gun clip', 'gun', 'grenade', 'hazmat jumpsuit', 'keys'}

    # created a nested dictionary for the rooms and items
    rooms = {
        'Waiting Room': {'North': 'Lounge Room'},
        'Lounge Room': {'North': 'Break Room', 'West': 'Wine Cellar', 'South': 'Waiting Room',
                        'item': 'night vision goggles'},
        'Wine Cellar': {'North': 'Basement', 'West': 'Theatre Room', 'East': 'Lounge Room', 'item': 'gun clip'},
        'Break Room': {'North': 'Main Office', 'West': 'Basement', 'South': 'Lounge Room', },
        'Main Office': {'South': 'Break Room', 'item': 'gun'},
        'Theatre Room': {'North': 'Lab', 'East': 'Wine Cellar'},
        'Lab': {'North': 'Conference Room', 'South': 'Theatre Room', 'item': 'treasure chest',
                'item1': 'hazmat jumpsuit'},
        'Conference Room': {'North': 'Office', 'South': 'Lab', 'East': 'Basement'},
        'Office': {'North': 'Vault Room', 'South': 'Conference Room', },
        'Vault Room': {'South': 'Office', 'East': 'Food Court', 'item': 'grenade'},
        'Food Court': {'South': 'Basement', 'East': 'Ball Room', 'West': 'Vault Room'},
        'Ball Room': {'West': 'Food Court', 'item': 'keys'},
        'Basement': {'North': 'Food Court', 'West': 'Conference Room', 'South': 'Wine Cellar', 'East': 'Break Room',
                     'item': 'Mega Spider'}
    }

    while True:
        print('---------------------------------------------------------------------------')
        print('Number of lives:', number_of_lives)
        print('You are in the', current_room)
        print()

        # iterate through each item in the inventory and then print....
        blank_str = ''
        for i in player_inventory:
            blank_str += i + ', '  # ....adding a comma and space
        print(f'Inventory:\n{blank_str[:-2]}')
        # converted inventory to a format string so that I can slice and
        # remove the last two characters, (comma and space)
        print()

        # notify the player when they collect all the items
        if len(player_inventory) == len(complete_inventory):
            print("You collected all of the items. It's time to hurry and defeat the Mega Spider!")
            print('The eggs are going to hatch soon!')
            print()

        # prompt player to enter a move and offer assistance for help
        user_input = input('Enter a move:\n')
        user_input = user_input.lower()

        while len(user_input.split()) != 2:  # to prevent player from entering less than or more than format "()()"
            print('Invalid move. Please enter a move command or enter "need help" for help.\n')
            user_input = input('Enter a move:\n')

        if user_input == 'need help':
            player_commands()
            continue

        print('---------------------------------------------------------------------------')

        # split the player's input into a list and then obtain the second object: the (direction) in ("go", "direction")
        command = user_input.split()
        v = command[0].capitalize()  # verb from input
        d = command[1].capitalize()  # direction from input
        direction = ['South', 'North', 'East', 'West']

        # if the direction from player input is in the current room
        if v == "Go" and d in rooms[current_room]:
            current_room = rooms[current_room][d]
            # the new current room is set to the direction of the current room
            # (pulling the d, direction key, from dictionary ...unlocks next location)

        # if the player's command is a valid input but no entrance
        elif v == "Go" and d not in rooms[current_room] and d in direction:
            print('There is no entrance in that direction, please enter another direction.')

        else:
            print('Invalid move. Please enter a move command or enter "need help" for help.')

        # The following conditions  are if the player runs into the mega spider
        if 'item' in rooms[current_room]:
            if rooms[current_room]['item'] == 'Mega Spider':
                if len(player_inventory) == 6:  # if the user collects all 6 items
                    print()
                    print('Look out!!! THE MEGA SPIDER')
                    print()
                    print('***crackling noises from eggs hatching***')
                    print('Hurry! Load your gun and kill the spider!')
                    user_input = input('Enter "shoot spider" to kill the spider:\n')
                    user_input = user_input.lower()
                    # used lower function so that no matter how the player types grab item, it will match
                    if user_input == 'shoot spider':
                        print('PEWW PEWWW PEWWWW. POP POP POP POP')
                        print()
                        print('***BOO000OOOOM*****')
                        print('---Mega spider collapses and dies---')
                        print()
                        print('***more crackling noises from eggs hatching open***')
                        print('Uh oh......throw the grenade and run out the exit !!')

                        user_input = input('Enter "throw grenade" to throw the grenade and run:\n')
                        user_input = user_input.lower()
                        if user_input == 'throw grenade':
                            print()
                            print("5, 4, 3, 2, 1..........")
                            print()
                            print()
                            print('***BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM*****')
                            print('Player escapes and wins.')
                            break

                        else:  # if the player misspells throw grenade
                            print('Last try! type "throw grenade" to throw the grenade.')
                            user_input = input()
                            user_input = user_input.lower()
                            if user_input != 'throw grenade':
                                print()
                                print('OHHHHH NOOOO! YOU MISSED!')
                                print('****thousands of mega spiders crawling out of eggs****')
                                print()
                                print('--grenade explodes with player inside building--')
                                print()
                                print('Number of lives: 0')
                                print('Player dies')
                                break
                            if user_input == 'throw grenade':
                                print("5, 4, 3, 2, 1..........")
                                print()
                                print()
                                print('***BOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOM*****')
                                print('Player escapes and wins.')
                                break
                    else:
                        print('You missed! Enter "shoot spider" to kill the spider:\n')
                        continue

                # if player runs into mega spider, does not collect all items, and does not have the special item
                if 'hazmat jumpsuit' not in player_inventory:
                    print()
                    print('AHHHH, LOOK OUT! The MEGA SPIDER!')
                    print()
                    print('***crackling noises from eggs hatching***')
                    print('ssssssssss ssss sssss')
                    print()
                    print('Number of lives:', (number_of_lives - 1))
                    print('Player dies. Game over')
                    break

                else:
                    # if player runs into mega spider, for the first time, while wearing hazmat suit
                    if 'hazmat jumpsuit' in player_inventory and number_of_lives == 2:
                        print()
                        print('AHHHH LOOK OUT! THE MEGA SPIDER')
                        print()
                        print('ssss ssss ss....')
                        print()
                        print('Whew! luckily you had on your suit.')
                        print('Last chance: hurry and the collect all of the items! The eggs will hatch soon!!!')
                        print('Number of lives:', (number_of_lives - 1))
                        number_of_lives = (number_of_lives - 1)

                        current_room = 'Lounge Room'
                        # player respawn
                        if current_room == 'Lounge Room':
                            user_input = input('Enter "ok" to continue:\n')
                            continue

                    # if player runs into mega spider again while wearing hazmat suit
                    if 'hazmat jumpsuit' in player_inventory and number_of_lives == 1:
                        print()
                        print('AHHHH NOT AGAIN! THE MEGA SPIDER!!!!!')
                        print()
                        print('ssss ssss ssSSSSSSSSSSSSSSSS SSSSSSSS!')
                        print()
                        print('zzzzzzzzzzz')
                        print('----eggs hatching open----')
                        print('Number of lives: 0')
                        print('Player dies.')
                        break

            # mandatory to pick up night vision goggles in first room
            if current_room == 'Lounge Room':
                if 'night vision goggles' not in player_inventory:
                    print("It's pitch black dark in here. Grab the night vision goggles to continue.")
                    while True:
                        user_input = input()
                        if user_input == 'grab item':
                            player_inventory.append(rooms[current_room].pop('item'))
                            # add and remove the item from the list
                            print('Night vision goggles added to inventory.')
                            break
                        else:
                            print(
                                "Invalid entry. Enter 'grab item' to pick up night vision goggles.")

            # special condition for room with treasure chest and special item
            elif rooms[current_room]['item'] == 'treasure chest':
                if 'hazmat jumpsuit' not in player_inventory: # prevents code below showing after player collects item
                    print()
                    print('There is a treasure chest in the room that contains an item.')
                    print('To unlock treasure chest, enter "unlock item" or "pass" to walk past the treasure chest')
                    user_input = input()
                    user_input = user_input.lower()
                    if user_input == 'unlock item':
                        if 'keys' not in player_inventory:
                            print('***Must find and grab "keys" to unlock treasure chest***')
                            print('---------------------------------------------------------------------------')

                        if 'keys' in player_inventory:
                            print('There is a hazmat jumpsuit inside.')
                            print('This special item protects you from the poisonous venom and '
                                  'gives you one additional life.')
                            print('However, this item does not protect you from explosions.')
                            user_input = input('Type "grab item" to put on the hazmat jumpsuit:\n')
                            user_input = user_input.lower()
                            if user_input == 'grab item':
                                player_inventory.append(rooms[current_room].pop('item1'))
                                number_of_lives += 1
                                print('Hazmat jumpsuit added to inventory')
                                print('---------------------------------------------------------------------------')
                            else:
                                print('Invalid entry. type "grab item" to grab item or treasure chest will close.')
                                user_input = input()
                                continue  # don't execute remaining code after continue, restart the loop again
                    if user_input == "pass":
                        print('You walked around the item.')

                    elif user_input != "pass" and user_input != "grab item" and user_input != "unlock item":
                        print('Invalid entry. type "grab item" to grab item or treasure chest will close.')
                        user_input = input()

            # notify player there's an item in the room and how to grab item
            elif 'item' not in player_inventory:
                print('There is an item in the room.')
                user_input = input()
                user_input = user_input.lower()
                if user_input == 'grab item':
                    print((rooms[current_room]['item']), 'added to inventory.')
                    player_inventory.append(rooms[current_room].pop('item'))
                    print('---------------------------------------------------------------------------')
                elif user_input == 'pass':
                    print('You walked around the item.')

                else:
                    while True:  # if player misspells entry or doesn't want to pick item up
                        user_input = input('Invalid entry. Enter "grab item" to grab item or "pass"  '
                                           'to walk around the item.\n')
                        user_input = user_input.lower()
                        if user_input == 'grab item':
                            print((rooms[current_room]['item']), 'added to inventory.')
                            player_inventory.append(rooms[current_room].pop('item'))
                            print('---------------------------------------------------------------------------')
                            break

                        elif user_input == 'pass':
                            print('You walked around the item.')
                            break
        print('---------------------------------------------------------------------------')

main()


# Professor: Grade: A 133.7/140
# Feedback: Your code needs to have comments that explain what and / or why you are doing something.
# The comment gives a brief summary of what the code is going to do and how it is being done.