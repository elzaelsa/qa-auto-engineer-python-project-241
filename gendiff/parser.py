import json

import yaml


def parse(data, extension):
    if extension == ".json":
        return json.loads(data)

    if extension in (".yml", ".yaml"):
        return yaml.safe_load(data)

    raise ValueError(f"Unsupported file format: {extension}")
