def set_alarm(employed, vacation):
    if employed and vacation:
        return False
    elif employed:
        return True
    else:
        return False