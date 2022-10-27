from Character import Character
from roll_modifier import roll_modifier
class Fighter(Character):
    def __init__(self, Name, alignment, ability_scores, xp):
        super().__init__(Name, alignment, ability_scores, xp)
        self.attack_roll_mod = 0 + int(self.level_number)
        self.hit_points = 5 + ((10 + roll_modifier(ability_scores[2])) * self.level_number)