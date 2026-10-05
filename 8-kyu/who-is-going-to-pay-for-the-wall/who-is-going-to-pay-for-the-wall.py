def who_is_paying(name):
    out = []
    if len(name)<=2:
        out.append(name)
        return out
    else:
        out.extend([name,name[:2]])
        return out