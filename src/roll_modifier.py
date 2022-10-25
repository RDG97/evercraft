def roll_modifier(ability_score):
    if ability_score == 1:
        return -5
    elif ability_score > 1 and ability_score < 4:
        return -4
    elif ability_score > 3 and ability_score < 6:
        return -3
    elif ability_score > 5 and ability_score < 8:
        return -2
    elif ability_score > 7 and ability_score < 10:
        return -1
    elif ability_score > 9 and ability_score < 12:
        return 0
    elif ability_score > 11 and ability_score < 14:
        return 1
    elif ability_score > 13 and ability_score < 16:
        return 2
    elif ability_score > 15 and ability_score < 18:
        return 3
    elif ability_score > 17 and ability_score < 20:
        return 4
    elif ability_score >= 20:
        return 5