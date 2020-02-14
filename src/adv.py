from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

item = {
    'coin': Item("coin", "20 Gold coins"),
    'sword': Item("sword", "For slaying Ogres")
}

# add items to rooms
room['foyer'].add_item_room(item['coin'], item['sword'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(' ', 'outside')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


name = input('Your name here: ')
current_room = room[player.current_room]
print(f'Hi! {name}. You are currently in {player.current_room}, {current_room.description}')
print(f"{current_room.view_items_room()}")



while True: 
    
    decision = input('Where would you like to go (South, North, East, West, Quit)?')
    decision = decision.lower()

    action = decision.split(' ')

    if (len(action) > 1) and (action[0] == 'take' or action[0] == 'get'):
        item = current_room.check_item_room(action[1])
        if item:
            print(item.on_take())
            player.add_item_inventory(item)
            current_room.remove_item_room(item.name)
        else:
            print("\nThis item is not in this room")
    elif len(action) > 1 and (action[0] == 'drop'):
        item = player.get_item_name(action[1])
        if item:
            print(item.on_drop())
            player.remove_item_inventory(item.name)
            current_room.add_item_room(item)
        else:
            print("\nThis item is not in your inventory")
    else:

    if decision == 'south'  and hasattr(current_room, "s_to"):
        current_room = current_room.s_to
        print(current_room)

    elif decision == 'north'  and hasattr(current_room, "n_to"):
        current_room = current_room.n_to
        print(current_room)

    elif decision == 'west' and hasattr(current_room, "w_to"):
        current_room = current_room.w_to
        print(current_room)

    elif decision == 'east' and hasattr(current_room, "e_to"):
        current_room = current_room.e_to
        print(current_room)
    
    elif decision == 'quit':
        print('Thank you for playing, come back soon!')
        break

    else: 
        print('Direction does not exist!')
    
    