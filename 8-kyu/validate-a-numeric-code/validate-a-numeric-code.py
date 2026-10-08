import re
​
def validate_code(code):
    pattern = r"^[1-3]"
    if re.match(pattern,str(code)):
        return True
    else:
        return False