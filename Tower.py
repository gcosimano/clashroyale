class Tower:
    def __init__(self, damage_per_sec, range, hitpoints, is_fallen, is_user):

        self.damage_per_sec = damage_per_sec
        self.range = range
        self.hitpoints = hitpoints
        self.is_fallen = is_fallen
        self.is_user = is_user

class KingTower(Tower):
    def __init__(self, damage_per_sec, range, hitpoints, is_fallen, is_active, is_user):
        super().__init__(damage_per_sec, range, hitpoints, is_fallen, is_user)
        self.is_active = is_active
