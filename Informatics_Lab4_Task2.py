def to_yaml(data):
    lines = []
    lines.append(f"day: {data['day']}")
    lines.append("lessons:")

    for lesson in data['lessons']:
        lines.append("  - time: " + lesson['time'])
        lines.append("    subject: " + lesson['subject'])
        lines.append("    room: " + lesson['room'])
        lines.append("    building: " + lesson['building'])
        lines.append("    format: " + lesson['format'])

    return "\n".join(lines)

yaml_text = to_yaml(data)

with open("schedule.yaml", "w", encoding="utf-8") as f:
    f.write(yaml_text)

print(yaml_text)

yaml_text = to_yaml(binary_object)

with open("schedule.yaml", "w", encoding="utf-8") as f:
    f.write(yaml_text)

print(yaml_text)