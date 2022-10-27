from Character import Character
from character_jobs import Fighter


def test_fighter_exists():
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    ryan = Fighter('Ryan', 'TheGoodGood', ability_scores, xp)
    assert ryan.is_alive == True

def test_fighter_has_attributes():
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 3000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    ryan = Fighter('Ryan', 'TheGoodGood', ability_scores, xp)
    assert ryan.attack_roll_mod == 3

def test_fighter_has_custom_hp():
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    ryan = Fighter('Ryan', 'TheGoodGood', ability_scores, xp)
    assert ryan.hit_points == 15

def test_custom_attributes():
    strength = 10
    dexterity = 10
    constitution = 10 
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    meme = Fighter('meme', 'bad guy', ability_scores, xp)
    assert meme.ability_scores[0] == 11

def test_custom_attributes():
    strength = 10
    dexterity = 10
    constitution = 10 
    wisdom = 10
    intelligence = 10
    charisma = 10
    xp = 1000
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    dabutcha = Butcher('dabutcha', 'best in the west', ability_scores, xp)