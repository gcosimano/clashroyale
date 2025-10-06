
class Card:
    
    def __init__(self, sc_key, elixir, type, combat_stats, damage, mechanics, counters, synergies):
        self.sc_key = sc_key
        self.elixir = elixir
        self.type = type
        self.combat_stats = combat_stats
        self.damage = damage
        self.mechanics = mechanics
        self.counters = counters
        self.synergies = synergies  
        self.x = None
        self.y = None 


    def setPos(self, newX, newY):
        self.x = newX
        self.y = newY
