def title_case(title, minor_words=''):
    s = title.split()
    minor_words = minor_words.lower().split()
    new = ""
    if not minor_words:
        for i in s:
            new+=i.capitalize()
            new+=" "
    else:
        for indx, i in enumerate(s):
            if i.lower() not in minor_words or indx==0:
                new+=i.capitalize()
                new+=" "
            else:
                new+=i.lower()
                new+=" "
​
    return new.rstrip(" ")