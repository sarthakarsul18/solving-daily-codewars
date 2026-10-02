def encode(st):
    en = ""
    v={
        "a": 1,
        "e": 2,
        "i": 3,
        "o": 4,
        "u": 5
    }
    for i in st:
        if i in v:
            en+=str(v.get(i))
        else:
            en+=i
    return en
​
​
            
            
    
def decode(st):
    de = ""
    vo = {
        1: "a",
        2: "e",
        3: "i",
        4: "o",
        5: "u"
        }
    
    for i in st:
        if i.isdigit():
            de += vo.get(int(i))
        else:
            de+=i
    return de