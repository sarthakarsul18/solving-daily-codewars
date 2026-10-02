import numpy as np
​
def data_reverse(data):
    group=[]
    for i in range(0,len(data),8):
        group.append(data[i:i+8])
        
    group.reverse()
​
    flat = np.array(group).flatten()
    return list(flat)