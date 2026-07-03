def row_weights(array):
    team1 = 0
    team2 = 0
​
    for i in range(len(array)):
        if i % 2 == 0:
            team1 += array[i]
        else:
            team2 += array[i]
​
    return (team1, team2)