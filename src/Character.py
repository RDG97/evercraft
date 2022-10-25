class Character:
    def __init__(self, Name, alignment):
        self.name = Name
        self.alignment = alignment
        self.hit_points = 5
        self.attack_points = 1
        self.is_alive = True
        self.xp = 0
        self.armour_class = 10
