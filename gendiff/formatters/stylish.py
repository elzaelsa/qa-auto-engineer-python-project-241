def stringify(value):
    if value is True:
        return "true"

    if value is False:
        return "false"

    return str(value)


def stylish(diff):
    result = ["{"]

    for item in diff:
        key = item["key"]
        status = item["status"]

        if status == "removed":
            result.append(f"  - {key}: {stringify(item['value'])}")

        elif status == "added":
            result.append(f"  + {key}: {stringify(item['value'])}")

        elif status == "unchanged":
            result.append(f"    {key}: {stringify(item['value'])}")

        elif status == "changed":
            result.append(f"  - {key}: {stringify(item['old_value'])}")
            result.append(f"  + {key}: {stringify(item['new_value'])}")

    result.append("}")

    return "\n".join(result)
