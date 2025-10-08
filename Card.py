
class Card:
    
    def __init__(self, sc_key, elixir, type, combat_stats, speed, counters, synergies, is_user):
        
        self.sc_key = sc_key
        self.x = None
        self.elixir = elixir
        self.type = type
        self.combat_stats = combat_stats
        self.speed = speed
        self.counters = counters
<<<<<<< HEAD
        self.synergies = synergies
        self.is_user = is_user
        self.path_list = path_list    
=======
        self.synergies = synergies  
        self.x = None
        self.y = None 
        


    def setPos(self, newX, newY):
        self.x = newX
        self.y = newY
>>>>>>> b26aa81 (add tower locations and place card method)
