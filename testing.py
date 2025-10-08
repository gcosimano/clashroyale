import get_data
import Card
import pprint
import json

troops = ['Musketeer', 'Knight', 'Archers', 'Giant', 'Minions', 'Mini Pekka', 'Spear Goblins', 'Goblins', 'Goblin Cage']
spells = ['Fireball', 'Arrows']

valid = troops + spells

deck = get_data.get_deck('data/', troops, spells)

if deck is not None:
    print("\n✅ Import successful! hello")
   # print(f"Data Type: {type(deck)}")
   # print(f"First 50 characters of data: {str(deck)[:50]}...\n")
else:
    print("❌ Import failed or file was not found.\n")

# Uncomment this to print entire deck
# pprint.pprint(get_data.get_deck('data/', troops, spells))

# making Decks with Card cards


file_path = 'troops.json'
with open(file_path, 'r') as file:
            json_data = json.load(file)

    # Each object in list is a Card object
user_deck = []
computer_deck = []

    # For every troop card
for x in json_data['troops']:
    if x['sc_key'] in valid:

        # Create the Card object 
        if 'damage' in x['combat_stats']:
            obj = Card.Card(x['sc_key'], x['elixir'], x['type'], x['combat_stats'], \
                    (x['mechanics']['speed']/60), x['counters'], x['synergies'], True) # type: ignore
        else:
            print(f"Warning: {x['sc_key']} has no damage stats!")
            obj = Card.Card(x['sc_key'], x['elixir'], x['type'], x['combat_stats'], \
                    {}, # Deal with this error somehow
                    (x['mechanics']['speed']/60), x['counters'], x['synergies'], True) # type: ignore
                    
                # Append to the list 
        user_deck.append(obj)   

for x in json_data['troops']:

     # Create the Card object 
    if x['sc_key'] in valid:
        if 'damage' in x['combat_stats']:
            obj = Card.Card(x['sc_key'], x['elixir'], x['type'], x['combat_stats'], \
                    (x['mechanics']['speed']/60), x['counters'], x['synergies'], False) # type: ignore
        else:
            print(f"Warning: {x['sc_key']} has no damage stats!")
            obj = Card.Card(x['sc_key'], x['elixir'], x['type'], x['combat_stats'], \
                    {}, # Deal with this error somehow
                    (x['mechanics']['speed']/60), x['counters'], x['synergies'], False) # type: ignore
            
        # Append to the list 
        computer_deck.append(obj)  


for x in user_deck:
    print(x.sc_key)