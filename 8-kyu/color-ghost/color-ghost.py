import random
class Ghost(object):
    def __init__(self):
        c = random.choice(["white","yellow","purple","red"])
        self.color = c
    