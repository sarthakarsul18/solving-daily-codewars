def number(lines):
    result = []
    if not lines:
        return []
    else:
        for i in range(1,len(lines)+1):
            result.append(f"{i}: {lines[i-1]}")
    return result         