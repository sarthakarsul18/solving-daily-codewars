def parse_float(string):
    if isinstance(string,float):
        return string
    else:
        try:
            return float(string)
        except (ValueError, TypeError):
            return None 