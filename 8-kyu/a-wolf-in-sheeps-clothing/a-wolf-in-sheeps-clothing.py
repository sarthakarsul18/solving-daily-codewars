def warn_the_sheep(queue):
    wolf_index = queue.index("wolf")
​
    if wolf_index == len(queue) - 1:
        return "Pls go away and stop eating my sheep"
​
    sheep_number = len(queue) - wolf_index - 1
    return f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!"