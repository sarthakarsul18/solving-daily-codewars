def is_vow(inp):
    v_code = [97, 101, 105, 111, 117]
    for indx, value in enumerate(inp):
        if value in v_code:
            inp[indx]=chr(value)
    return inp