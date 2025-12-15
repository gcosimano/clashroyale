import json
from Card import Card
from Board import Board
import time
import os

class OneCardRunner:
    file_path = 'troops.json'
    with open(file_path, 'r') as file:
            json_data = json.load(file)

    # Each object in list is a Card object
    list_of_objects = []

    troops = ['Musketeer', 'Knight', 'Archers', 'Giant', 'Minions', 'Mini Pekka', 'Spear Goblins', 'Goblins', 'Goblin Cage']

    # For every troop card
    for x in json_data['troops']:

        if x['sc_key'] in troops:

            # Create the Card object 
            if 'damage' in x['combat_stats']:
                obj = Card(x['sc_key'], x['elixir'], x['type'], x['combat_stats'], x['mechanics']['attack_radius'], x['mechanics']['sight_range'], x['mechanics']['speed'], x['counters'], x['synergies'], True, 0) # type: ignore
                # print(obj)
            else:
                print(f"Warning: {x['sc_key']} has no damage stats!")
                obj = Card(x['sc_key'], x['elixir'], x['type'], x['combat_stats'], x['mechanics'], x['counters'], x['synergies'], True, 0) # type: ignore
            
            # Append to the list 
            list_of_objects.append(obj)        

    # print(list_of_objects)
    # Creates 18x32 game board array

    board = Board()

    card1: Card = list_of_objects[0]
    board.place_card(card1, 30, 1)


    start_time = time.monotonic() 
    elapsed = 0       

    while elapsed < 4:
        current_time = time.monotonic()
        new_elapsed = round((current_time - start_time),1)
        if new_elapsed > elapsed:
            elapsed = new_elapsed
        if elapsed == card1.time_since_moved + 1:
             
            board.move_card(card1, elapsed)
<<<<<<< HEAD
            #board.print_board()
            print(card1.time_since_moved)

            # print(elapsed, "seconds have elapsed.")
=======
            board.print_board()

            print(elapsed, "seconds have elapsed.")
>>>>>>> f88c5a4bf17946f3d4d7fc4057218c0452dd4ef4
        time.sleep(.1)
        
