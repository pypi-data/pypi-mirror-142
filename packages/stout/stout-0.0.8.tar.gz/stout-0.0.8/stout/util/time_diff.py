from datetime import datetime

def time_diff(past, future, fmt='%Y-%m-%d', interval='days'):
    '''
    from stout.util import path_import

    time_diff('2020-10-10', '2021-10-10')
    '''
    return ((
        future if type(future) == datetime else datetime.strptime(future, fmt)
    ) - (
        past if type(past) == datetime else datetime.strptime(past, fmt)
    )).__getattribute__(interval)