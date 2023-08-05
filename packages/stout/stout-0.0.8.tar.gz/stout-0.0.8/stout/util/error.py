from traceback import format_exc

def detailed_error():
    ''' 
    from stout.util.error import detailed_error

    try: create_error()
    except:
            
        err = detailed_error()
        print(err)
    '''
    return format_exc().splitlines()