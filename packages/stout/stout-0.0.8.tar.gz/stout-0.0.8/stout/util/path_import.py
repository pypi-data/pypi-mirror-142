from importlib.util import module_from_spec, spec_from_file_location

def path_import(_name, _path):
    '''
    from stout.util import path_import

    module = path_import('module', 'path/to/file.py')
    module.func(...)
    '''
    try:
        spec = spec_from_file_location(_name, _path)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
    except FileNotFoundError: raise Exception(f'Module Not Imported! File Not Found: "{_path}"')
    return module