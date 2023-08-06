def boolean(value):
    if isinstance(value, int) or isinstance(value, float):
        value = False if value == 0 else True
    elif isinstance(value, bool):
        pass
    elif isinstance(value, str):
        if value.isdigit():
            value = False if float(value) == 0 else True
        else:
            try:
                value = float(value)
                value = False if value == 0 else True
            except:
                value = False if value == 'false' else True
    elif value is not None:
        value = True
    else:
        value = False
    return value
