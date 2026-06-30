def capitalize(s):
    even=""
    odd=""
    for idx, chr in enumerate(s):
        if idx%2==0:
            chr = chr.upper()
            even+=chr
            chr = chr.lower()
            odd+=chr
        else:
            chr = chr.lower()
            even+=chr
            chr = chr.upper()
            odd+=chr
    return[even,odd]
            
        
        