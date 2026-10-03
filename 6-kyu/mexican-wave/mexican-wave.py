def wave(people):
    new=[]
    for i in range(0,len(people)):
        if people[i] == " ":
            continue
        wave_str = people[:i] + people[i].upper() + people[i+1:]
        new.append(wave_str)
    return new