geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
​
def goose_filter(birds):
    new = []
    for i in birds:
        if i not in geese:
            new.append(i)
    return new