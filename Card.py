
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
        self.x = None
        self.y = None 
        


    def setPos(self, newX, newY):
        self.x = newX
        self.y = newY
 
    def to_string(self):
       COLOR = ""
       RESET = '\033[0m'
       if(self.is_user == True):
           COLOR = "\033[91m"
       else:
           COLOR = "\033[94m"
       first_letter = self.sc_key[0]
       if(self.sc_key == "goblin"):
           first_letter = "g"
       ans = f"{COLOR}{first_letter}{RESET}"
       return ans

