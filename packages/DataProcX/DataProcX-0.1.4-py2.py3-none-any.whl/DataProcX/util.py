def debug(func):
    """wrapper @debug"""
    def wrapper(*args, **kwargs):
        print("[DEBUG]: enter {}()".format(func.__name__))
        return func(*args, **kwargs)
    return wrapper