from Character import Character
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
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]

    character = Character(name, alignment, ability_scores)
    assert character.name != None

def test_character_alignment():
    name = 'Ryan'
    alignment = 'good'
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    character = Character(name, alignment, ability_scores)
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
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    character = Character(name, alignment, ability_scores)
    assert character.hit_points > 0

def test_character_attack_points():
    name = 'Ryan'
    alignment = 'good'
    strength = 10
    dexterity = 10
    constitution = 10
    wisdom = 10
    intelligence = 10
    charisma = 10
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    character = Character(name, alignment, ability_scores)
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
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    character = Character(name, alignment, ability_scores)
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
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    character = Character(name, alignment, ability_scores)
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
    ability_scores = [strength, dexterity, constitution, wisdom, intelligence, charisma]
    character = Character(name, alignment, ability_scores)
    assert len(character.ability_scores) == 6 
