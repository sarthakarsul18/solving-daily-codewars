def hello(name=""):
    if name is None or len(name)==0:
        return "Hello, World!"
    else:
        return f"Hello, {name.capitalize()}!"