import get_data
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
for i in range(12):
    sc_key = d[i["sc_key"]]
    type = d[i["type"]]
    elixir = d[i["elixir"]]
    combat = d[i["combat_stats"]]
    damage = d[i["damage"]]
    mechanics = d[i["mechanics"]]
    synergies = d[i["synergies"]]
    counters = d[i["counters"]]
    d.append(Card(sc_key, elixir, type, combat, damage, mechanics, counters, synergies))

print(deck)



