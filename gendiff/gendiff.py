from pathlib import Path

from gendiff.formatters.json import json_format
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.parser import parse


def generate_diff(file_path1, file_path2, formatter="stylish"):
    data1 = read_file(file_path1)
    data2 = read_file(file_path2)

    diff = build_diff(data1, data2)

    if formatter == "stylish":
        return stylish(diff)

    if formatter == "plain":
        return plain(diff)
    
    if formatter == "json":
        return json_format(diff)

    raise ValueError(f"Unknown formatter: {formatter}")


def read_file(file_path):
    extension = Path(file_path).suffix

    with open(file_path) as file:
        content = file.read()

    return parse(content, extension)


def build_diff(data1, data2):
    keys = sorted(set(data1) | set(data2))
    diff = []

    for key in keys:
        if key not in data2:
            diff.append(
                {
                    "key": key,
                    "status": "removed",
                    "value": data1[key],
                }
            )
        elif key not in data1:
            diff.append(
                {
                    "key": key,
                    "status": "added",
                    "value": data2[key],
                }
            )
        elif data1[key] == data2[key]:
            diff.append(
                {
                    "key": key,
                    "status": "unchanged",
                    "value": data1[key],
                }
            )
        else:
            diff.append(
                {
                    "key": key,
                    "status": "changed",
                    "old_value": data1[key],
                    "new_value": data2[key],
                }
            )

    return diff
