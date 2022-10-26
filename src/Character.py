from roll_modifier import roll_modifier
class Character:
    strength = 10
    dexterity = 10
    constitution = 10 
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 0
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    def __init__(self, Name, alignment, ability_scores, xp):
        self.name = Name
        self.alignment = alignment
        self.attack_points = 1
        self.is_alive = True
        self.level_number =(xp // 1000)
        self.hit_points = 5 + ((5 + roll_modifier(ability_scores[2])) * self.level_number)
        self.armour_class = 10
        self.ability_scores = ability_scores
    def attack(self, target1, target2, roll):
        if roll == 20:
            return setattr(target2, 'hit_points', (int(target2.hit_points) - (int(target1.attack_points) * 2))), setattr(target1, 'xp', + 10)
        elif roll < 20 and roll > 0:
            return setattr(target2, 'hit_points', (int(target2.hit_points) - (int(target1.attack_points)))), setattr(target1, 'xp', + 10)
        elif roll == 0:
            print('you really suck')
