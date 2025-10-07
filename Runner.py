import json
from Card import Card

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
                       (x['mechanics']['speed']/60), x['counters'], x['synergies'], True) # type: ignore
        else:
            print(f"Warning: {x['sc_key']} has no damage stats!")
            obj = Card(x['sc_key'], x['elixir'], x['type'], x['combat_stats'], \
                       {}, # Deal with this error somehow
                       (x['mechanics']['speed']/60), x['counters'], x['synergies'], True) # type: ignore
            
        # Append to the list 
        list_of_objects.append(obj)        
