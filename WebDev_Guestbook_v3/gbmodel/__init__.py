model_backend = 'pylist'
#model_backend = 'sqlite3'

def get_model():
    if model_backend == 'sqlite3':
        from .model_sqlite3 import model
    elif model_backend == 'pylist':
        from .model_pylist import model
    else:
        raise ValueError("No appropriate databackend configured. ")
    return model()