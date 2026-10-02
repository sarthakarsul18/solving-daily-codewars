def duck_duck_goose(players, goose):
    index = (goose - 1) % len(players)   
    return players[index].name