def stairs_in_20(stairs):
    years = 0
    for i in stairs:
        years+=sum(i)
    return years*20