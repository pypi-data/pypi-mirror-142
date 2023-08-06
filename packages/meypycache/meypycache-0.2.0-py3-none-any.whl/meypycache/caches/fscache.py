from ..core.uuid import uuid_from_func
from ..core.files import load_object, save_object
from typing import Optional
from loguru import logger
from pathlib import Path
from ..core.paramconverter import ParameterConverter

def _fscache(func, directory='./.tmp', paramconverter: Optional[ParameterConverter] = None, json:bool = True):
    def wrapper(*args, **kwargs):
        arg_ids = {} if arg_ids is None else arg_ids
        kwarg_ids = {} if kwarg_ids is None else kwarg_ids

        filename = uuid_from_func(func, args, kwargs, paramconverter=paramconverter)

        path = Path(directory)/filename
        filetype = 'json' if json else 'pickle'

        if path.exists():
            try:
                logger.debug(f"Loading cached method {filename}")
                return load_object(path, type=filetype)
            except:
                logger.error(f"Could not load cached method {filename} rerunning method")

        rtn = func(*args, **kwargs)

        logger.debug(f"Caching method {filename}")
        save_object(rtn, path, type = filetype)

        return rtn
    return wrapper

def fscache(func=None, *args, **kwargs):
    if func is None:
        def wrapper(_func):
            return _fscache(_func, *args, **kwargs)
        return wrapper
    return _fscache(func, *args, **kwargs)
