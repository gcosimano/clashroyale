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
# pprint.pprint(get_deck('data/', troops, spells))
