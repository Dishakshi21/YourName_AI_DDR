def merge_data(data1, data2):

    if isinstance(data1, dict):
        data1 = [data1]

    if isinstance(data2, dict):
        data2 = [data2]

    merged = data1 + data2

    # remove duplicates
    seen = set()
    unique = []

    for item in merged:
        area = item.get("area", "unknown")
        if area not in seen:
            seen.add(area)
            unique.append(item)

    return unique