def how_much_i_love_you(nb_petals):
    phrase = [
        "I love you",
        "a little",
        "a lot",
        "passionately",
        "madly",
        "not at all"
    ]
​
    return phrase[(nb_petals - 1) % 6]