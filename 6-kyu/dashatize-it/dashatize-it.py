def dashatize(n):
    new = ""
    for indx, i in enumerate(str(abs(n))):
        if int(i) % 2 == 0:
            new += i
        else:
            if new and new[-1] != "-":
                new += "-"
            new += i
            new += "-"
    
    return new.rstrip("-")