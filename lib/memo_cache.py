import logging

def memo(f):
    f.cache = {}
    def _f(*args, **kwargs):
        key = __get_cache_key__(args, f)
        if key not in f.cache:
            f.cache[key] = f(*args, **kwargs)
        else:
            logging.info(f"Cache hit for {f.__name__}")
        return f.cache[key]
    return _f

def __get_cache_key__(args, f):
    if(len(args) > 0 and hasattr(args[0], f.__name__)):
        return args[1:]
    return args