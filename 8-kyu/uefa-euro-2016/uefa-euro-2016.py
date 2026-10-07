def uefa_euro_2016(teams, scores):
    if scores[0]>scores[1]:
        return f"At match {teams[0]} - {teams[1]}, {teams[0]} won!"
    elif scores[0]==scores[1]:
        return f"At match {teams[0]} - {teams[1]}, teams played draw."
    else:
        return f"At match {teams[0]} - {teams[1]}, {teams[1]} won!"