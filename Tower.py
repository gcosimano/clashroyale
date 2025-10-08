class Tower:
    def __init__(self, damage_per_sec, range, hitpoints, is_fallen):

        self.damage_per_sec = damage_per_sec
        self.range = range
        self.hitpoints = hitpoints
        self.is_fallen = is_fallen

class KingTower(Tower):
    def __init__(self, damage_per_sec, range, hitpoints, is_fallen, is_active):
        super().__init__(damage_per_sec, range, hitpoints, is_fallen)
        self.is_active = is_active
