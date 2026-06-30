def combat(health, damage):
    health = health - damage
    if health<0:
        health = 0
        return health
    else:
        return health