class Character:
    strength = 10
    # strength_mod = strength + mod
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    def __init__(self, Name, alignment, ability_scores):
        self.name = Name
        self.alignment = alignment
        self.hit_points = 5
        self.attack_points = 1
        self.is_alive = True
        self.xp = 0
        self.armour_class = 10
        self.ability_scores = ability_scores
