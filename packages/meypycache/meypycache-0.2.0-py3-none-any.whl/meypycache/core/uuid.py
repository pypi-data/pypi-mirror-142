from typing import Callable, Tuple, Mapping, Any, Optional
import uuid
import random
from inspect import getsource
import json
from .paramconverter import ParameterConverter

def uuid_from_seed(seed):
    rd = random.Random()
    rd.seed(seed)

    return uuid.UUID(int=rd.getrandbits(128))

Args = Tuple[Any, ...]
Kwargs = Mapping[str, Any]
Transform = Callable[[Any], str]

def uuid_from_func(
    func: Callable, 
    args: Args, 
    kwargs: Kwargs, 
    paramconverter: Optional[ParameterConverter] = None,
    metadata: str = ''
):
    args = list(tuple)
    kwargs = kwargs.copy()

    if paramconverter is not None:
        links = paramconverter.serialize_convert(func, args, kwargs)
    else:
        links = {'args':args, 'kwargs':kwargs}

    id_metadata = {
        'func': getsource(func),
        'links': links,
        'metadata': metadata
    }

    id_metadata_serialized = json.dumps(id_metadata)

    return uuid_from_seed(id_metadata_serialized)
