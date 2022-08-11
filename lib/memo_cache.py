def memo(f):
    f.cache = {}
    def _f(*args, **kwargs):
        key = __get_cache_key__(args, f)
        if key not in f.cache:
             response = f(*args, **kwargs)
             if(response is not None):
                 f.cache[key] = response
             else: 
                return None   
        return f.cache[key]
    return _f

def __get_cache_key__(args, f):
    if(len(args) > 0 and hasattr(args[0], f.__name__)):
        return args[1:]
    return args