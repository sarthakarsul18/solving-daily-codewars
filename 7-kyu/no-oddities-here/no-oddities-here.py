def no_odds(values):
    new = []
    for i in values:
        if i%2==0 or i==0:
            new.append(i)
    return new