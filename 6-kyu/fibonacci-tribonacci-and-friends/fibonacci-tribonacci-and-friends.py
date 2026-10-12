def xbonacci(signature,n):
    l = len(signature)
    for i in range(n):
        if len(signature)<n:
            signature.append(sum(signature[-l:]))
    return signature[:n]