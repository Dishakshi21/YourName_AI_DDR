def validate(data):
    if not data:
        return {
            "data": "Not Available",
            "conflicts": ["No data available"]
        }

    conflicts = []

    for item in data:
        obs = str(item.get("observation", "")).lower()
        temp = str(item.get("temperature", "")).lower()

        if "no issue" in obs and ("high" in temp or "heat" in temp):
            conflicts.append(f"Conflict detected in {item.get('area', 'Unknown')}")

    if not conflicts:
        conflicts = ["No conflicts found"]

    return {
        "data": data,
        "conflicts": conflicts
    }