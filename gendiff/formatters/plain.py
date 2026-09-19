def stringify(value):
    if value is True:
        return "true"

    if value is False:
        return "false"

    if value is None:
        return "null"

    if isinstance(value, str):
        return f"'{value}'"

    return str(value)


def plain(diff):
    result = []

    for item in diff:
        key = item["key"]
        status = item["status"]

        if status == "removed":
            result.append(f"Property '{key}' was removed")

        elif status == "added":
            value = stringify(item["value"])
            result.append(
                f"Property '{key}' was added with value: {value}"
            )

        elif status == "changed":
            old_value = stringify(item["old_value"])
            new_value = stringify(item["new_value"])

            result.append(
                f"Property '{key}' was updated. "
                f"From {old_value} to {new_value}"
            )

    return "\n".join(result)