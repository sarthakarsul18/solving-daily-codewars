import math
​
def nearest_sq(n):
    sqr = math.sqrt(n)
    fl = math.floor(sqr)
    ce = math.ceil(sqr)
    sqr_fl = fl**2
    sqr_ce = ce**2
    if abs(n-sqr_fl)<abs(n-sqr_ce):
        return sqr_fl
    else:
        return sqr_ce