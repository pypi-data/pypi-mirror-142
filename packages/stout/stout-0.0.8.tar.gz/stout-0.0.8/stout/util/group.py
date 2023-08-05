def group():
    ''' 
    from stout.util import group

    g = group()

    @g
    def a(): ...

    @g
    def b(): ...

    @g
    def c(): ...

    if __name__ == '__main__':
        for f in g.available: f()
    '''
    functions = []
    def handler(func):functions.append(func)
    handler.functions = functions
    return handler