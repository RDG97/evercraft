def attack(target1, target2, roll):
    if roll == 20:
        return int(target2.hit_points) - (int(target1.attack_points) * 2)
    elif roll < 20 and roll > 0:
        return int(target2.hit_points) - int(target1.attack_points)
    elif roll == 0:
        print('you really suck')
