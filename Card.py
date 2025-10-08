
class Card:
    
    def __init__(self, sc_key, elixir, type, combat_stats, speed, counters, synergies, is_user):
        
        self.sc_key = sc_key
        self.elixir = elixir
        self.type = type
        self.combat_stats = combat_stats
        self.speed = speed
        self.counters = counters
        self.synergies = synergies
        self.is_user = is_user
        self.path_list = path_list    
