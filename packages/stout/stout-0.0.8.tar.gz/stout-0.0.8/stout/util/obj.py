def nested_set(_obj, _keys, _value):
    '''
    from stout.util.obj import nested_set

    obj = {'a':{'b':{'c':'hello'}}}
    nested_set(obj, ['a','b','c'], 'world')
    '''
    for key in _keys[:-1]:
        _obj = _obj.setdefault(key, {})
    _obj[_keys[-1]] = _value

def nested_get(_obj, _keys):
    '''
    from stout.util.obj import nested_get

    obj = {'a':{'b':{'c':'hello'}}}
    nested_get(obj, ['a','b','c'])
    '''
    nobj = _obj
    for key in _keys:
        nobj = nobj.get(key)
        if not nobj: return None
    return nobj
