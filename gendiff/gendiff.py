import json


def stringify(value):
    if value is True:
        return "true"
    if value is False:
        return "false"
    return str(value)


def generate_diff(file_path1, file_path2):
    with open(file_path1) as file:
        data1 = json.load(file)

    with open(file_path2) as file:
        data2 = json.load(file)

    keys = sorted(set(data1) | set(data2))

    result = ["{"]

    for key in keys:
        if key not in data2:
            result.append(f"  - {key}: {stringify(data1[key])}")
        elif key not in data1:
            result.append(f"  + {key}: {stringify(data2[key])}")
        elif data1[key] == data2[key]:
            result.append(f"    {key}: {stringify(data1[key])}")
        else:
            result.append(f"  - {key}: {stringify(data1[key])}")
            result.append(f"  + {key}: {stringify(data2[key])}")

    result.append("}")

    return "\n".join(result)