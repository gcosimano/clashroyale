import get_data
import Card
import pprint

troops = ['Musketeer', 'Knight', 'Archers', 'Giant', 'Minions', 'Mini Pekka', 'Spear Goblins', 'Goblins', 'Goblin Cage']
spells = ['Fireball', 'Arrows']

deck = get_data.get_deck('data/', troops, spells)

if deck is not None:
    print("\n✅ Import successful!")
    print(f"Data Type: {type(deck)}")
    print(f"First 50 characters of data: {str(deck)[:50]}...\n")
else:
    print("❌ Import failed or file was not found.\n")

# Uncomment this to print entire deck
# pprint.pprint(get_data.get_deck('data/', troops, spells))

# making Decks with Card cards
d = get_data.get_deck('data/', troops, spells)
deck = []
for i in range(len(d)):
    sc_key = d[i]["sc_key"]
    type = d[i]["type"]
    elixir = d[i]["elixir"]
    combat = d[i]["combat_stats"]

    if 'damage' in d[i]['combat_stats']:
        damage = d[i]["combat_stats"]['damage']
    else:
        damage = {}

    mechanics = d[i]["mechanics"]
    synergies = d[i]["synergies"]
    counters = d[i]["counters"]
    a = Card.Card(sc_key, elixir, type, combat, mechanics, damage, counters, synergies)
    deck.append(a)

# Each element of the deck list is a Card object and not a dictionary
print(deck[0].sc_key)



