def iter_chunks(_list, _chunk_size):
    '''
    from stout.util import iter_chunks

    for chunk in iter_chunks([ ... ], 10): 
        ...
    '''
    for i in range(0, len(_list), _chunk_size):
        yield _list[i:i+_chunk_size]