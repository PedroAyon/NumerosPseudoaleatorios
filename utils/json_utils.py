import json


def read_json_file(filepath):
    with open(filepath) as f:
        data = json.load(f)
    return data


def write_json_file(filepath, data):
    with open(filepath, "w+") as f:
        f.truncate(0)
        json.dump(data, f, indent=2)
    print(f'Archivo guardado en: {filepath}')
