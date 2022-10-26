from Character import Character
from roll_modifier import roll_modifier
from attack import attack

def test_character():
    assert Character != None

def test_character_attribute():
    name = 'Ryan'
    alignment = 'good man'
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]

    character = Character(name, alignment, ability_scores, xp)
    assert character.ability_scores[0] == 10

def test_character_alignment():
    name = 'Ryan'
    alignment = 'good'
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    character = Character(name, alignment, ability_scores, xp)
    assert character.alignment != None

def test_character_hit_points():
    name = 'Ryan'
    alignment = 'good'
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    character = Character(name, alignment, ability_scores, xp)
    assert (getattr(character, 'hit_points')) == 10

def test_character_attack_points():
    name = 'Ryan'
    alignment = 'good'
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    character = Character(name, alignment, ability_scores, xp)
    assert character.attack_points > 0

def test_is_alive():
    name = 'Ryan'
    alignment = 'good'
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    character = Character(name, alignment, ability_scores, xp)
    assert character.is_alive == True

def test_xp():
    name = 'Ryan'
    alignment = 'good'
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    character = Character(name, alignment, ability_scores, xp)
    assert character.xp >= 0

def test_armour_class():
    name = 'Ryan'
    alignment = 'good'
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    character = Character(name, alignment, ability_scores)
    assert character.armour_class > 0

def test_armour_class():
    name = 'Ryan'
    alignment = 'good'
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    character = Character(name, alignment, ability_scores, xp)
    assert len(character.ability_scores) == 6 

def test_roll_modifier1():
    assert roll_modifier(1) == -5

def test_roll_modifier3():
    assert roll_modifier(3) == -4

def test_roll_modifier5():
    assert roll_modifier(5) == -3

def test_roll_modifier6():
    assert roll_modifier(6) == -2

def test_roll_modifier9():
    assert roll_modifier(9) == -1

def test_roll_modifier11():
    assert roll_modifier(11) == 0

def test_roll_modifier12():
    assert roll_modifier(12) == 1

def test_roll_modifier14():
    assert roll_modifier(14) == 2

def test_roll_modifier12():
    assert roll_modifier(12) == 1
    
def test_roll_modifier14():
    assert roll_modifier(14) == 2

def test_roll_modifier16():
    assert roll_modifier(16) == 3

def test_roll_modifier19():
    assert roll_modifier(19) == 4

def test_roll_modifier20():
    assert roll_modifier(20) == 5
    
def test_attack():
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    roll = 10
    Morgan = Character('Morgan', 'Good', ability_scores, xp)
    Keith = Character('Keith', 'Evil', ability_scores, xp)
    attack_value = attack(Morgan, Keith, roll)
    setattr(Keith, 'hit_points', attack_value)
    assert getattr(Keith, 'hit_points') == 9

def test_character_attack_crit():
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    attacker = Character('morgan', 'good', ability_scores, xp)
    defender = Character('keith', 'evil', ability_scores, xp)
    attacker.attack(attacker, defender, 20)
    assert getattr(defender, 'hit_points') == 8

def test_character_attack():
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    attacker = Character('morgan', 'good', ability_scores, xp)
    defender = Character('keith', 'evil', ability_scores, xp)
    attacker.attack(attacker, defender, 13)
    assert getattr(defender, 'hit_points') == 9

def test_xp_growth():
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    attacker = Character('morgan', 'good', ability_scores, xp)
    defender = Character('keith', 'evil', ability_scores, xp)
    attacker.attack(attacker, defender, 13)
    assert getattr(attacker, 'xp') == 10

def test_level():
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    lvlboi = Character('lvlboi', 'the best', ability_scores, 1024)
    #setattr(lvlboi, 'xp', 1024)
    assert getattr(lvlboi, 'level_number') == 1
    
def test_level():
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 2600
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    yomom = Character('Fatty', 'Food', ability_scores, xp)
    assert getattr(yomom, 'level_number') == 2

def test_level_modification():
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 2600
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    jerkFace = Character('Ryan', 'Cajun', ability_scores, xp)
    assert getattr(jerkFace, 'hit_points') == 15# character = level_up(character)

def test_attack_mod():
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 0
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    thiccboy = Character('Tyler', 'TheThickening', ability_scores, xp)
    attackModder(thiccboy)
    assert thiccboy.attack_roll_mod == 1
