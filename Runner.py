import json
from Card import Card
from Board import Board

class Runner:
    file_path = 'troops.json'
    with open(file_path, 'r') as file:
            json_data = json.load(file)

    # Each object in list is a Card object
    list_of_objects = []

    # For every troop card
    for x in json_data['troops']:

        # Create the Card object 
        if 'damage' in x['combat_stats']:
            obj = Card(x['sc_key'], x['elixir'], x['type'], x['combat_stats'], \
                       x['combat_stats'].get('damage', {}),
                       x['mechanics'], x['counters'], x['synergies']) # type: ignore
        else:
            print(f"Warning: {x['sc_key']} has no damage stats!")
            obj = Card(x['sc_key'], x['elixir'], x['type'], x['combat_stats'], \
                       {}, # Deal with this error somehow
                       x['mechanics'], x['counters'], x['synergies']) # type: ignore
            
        # Append to the list 
        list_of_objects.append(obj)        


# Creates 18x32 game board array
board = Board()

test_card = Card("Knight", 3, "Troop", {"hitpoints": 600}, {"damage": 75}, ["Ground"], ["Valkyrie"], ["Giant"])
board.place_card(test_card, 5, 10)


'''
king tower (player side) - (8-11, 2-5)
princess tower left (player side) - (3-5, 6-8)
princess tower right (player side) - (14-16, 6-8)
king tower (opponent side) - 
princess tower left (opponent side) - 
princess tower right (opponent side) - 
river - (1-18, 16-17)
'''



# 32x15
# create a 2D array to represent the board
# place towers on board (make sure each point of the tower points to the same object)
# place paths on board
# place rivers/bridges on board
# place card method for x and y
# card automatically goes to left or right bridge depending on which is closer
# if card is place on y coord below or equal to towers, it goes straight up past them, diagonal to path, and straight up path