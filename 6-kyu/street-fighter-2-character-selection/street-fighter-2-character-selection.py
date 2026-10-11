​
def street_fighter_selection(fighters, initial_position, moves):
    row, col = initial_position
    result = []
​
    for move in moves:
        if move == "up":
            row = max(0, row - 1)
        elif move == "down":
            row = min(1, row + 1)
        elif move == "left":
            col = (col - 1) % 6
        elif move == "right":
            col = (col + 1) % 6
​
        result.append(fighters[row][col])
​
    return result
​