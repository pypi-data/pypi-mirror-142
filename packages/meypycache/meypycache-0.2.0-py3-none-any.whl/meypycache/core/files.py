import json
import yaml
import pickle

FileType = str

def save_object(obj, path, type: FileType = 'json'):
    if type == 'json':
        with open(path, 'w') as f:
            json.dump(obj, f)
    elif type == 'yaml':
        with open(path, 'w') as f:
            yaml.save_dump(obj, f)
    elif type == 'pickle':
        with open(path, 'wb') as f:
            pickle.dump(obj, f)

def load_object(path, type: FileType = 'json'):
    if type == 'json':
        with open(path, 'r') as f:
            return json.load(f)
    elif type == 'yaml':
        with open(path, 'r') as f:
            return yaml.save_load(f)
    elif type == 'pickle':
        with open(path, 'rb') as f:
            return pickle.load(f)
