def solve(s):
    l = ""
    u = ""
    for i in s:
        if i.islower():
            l+=i
        else:
            u+=i
    
    if len(l)==len(u) or len(l)>len(u):
        return s.lower()
    else:
        return s.upper()
        
            