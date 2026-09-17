def alphabet_war(f):
    p={'w':4,'p':3,'b':2,'s':1,'m':-4,'q':-3,'d':-2,'z':-1}
    x=sum(p.get(c,0) for c in f)
    return "Left side wins!" if x>0 else "Right side wins!" if x<0 else "Let's fight again!"