def stock_list(stocklist, categories):
    if not stocklist or not categories:
        return ""
​
    result = [(c, 0) for c in categories]
​
    for i in stocklist:
        code, num = i.split()
​
        for index, c in enumerate(categories):
            if code[0] == c:
                result[index] = (c, result[index][1] + int(num))
​
    return " - ".join(f"({c} : {num})" for c, num in result)