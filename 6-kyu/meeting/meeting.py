def meeting(s):
    s = s.upper()
    full_name = s.split(";")
    merge_n = []
    for i in full_name:
        first,last = i.split(":")
        merge_n.append((last,first))
                       
    merge_n.sort()
​
    final = ""
    for last,first in merge_n:
         final += f"({last}, {first})"
    return final.upper()