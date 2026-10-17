def show_sequence(n):
    result = []
    total = 0
    if n<0:
        return f"{n}<0"
    elif n==0:
        return "0=0"
    else:
        for i in range(n+1):
            result.append((str(i)))
            total+=i
            
        final = "+".join(result)
        final_result = final+" = "+str(total)
    return final_result
​