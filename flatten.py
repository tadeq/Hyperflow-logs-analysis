from pathlib import Path
import sys
from pandas.io.json import json_normalize
import json

def flatten_json(y):
    out = {}
    def flatten(obj, name=''):
        if type(obj) is dict:
            for part in obj:
                flatten(obj[part], name + part + '.')
        else:
            out[name[:-1]] = obj
    flatten(y)
    return out

directory_to_clean = './'
jsonl_files = [path for path in Path(directory_to_clean).rglob('*.jsonl')]

for ind, file in enumerate(jsonl_files):
    print('{}/{}'.format(ind, len(jsonl_files)))
    flattened = ''
    with open(file) as f:
        for json_obj in f:
            flattened += json.dumps(flatten_json(json.loads(json_obj))) + '\n'
    with open(file, 'w') as f:
        f.write(flattened)