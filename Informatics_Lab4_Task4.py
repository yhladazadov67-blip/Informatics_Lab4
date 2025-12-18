def parse_hcl(text):
    result = {}
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    i = 0

    while i < len(lines):
        line = lines[i]

        if '=' in line and not line.startswith('lessons'):
            key, value = line.split('=', 1)
            result[key.strip()] = value.strip().strip('"')

        elif line.startswith('lessons'):
            i += 1
            lessons = []

            while not lines[i].startswith(']'):
                if lines[i].startswith('{'):
                    lesson = {}
                    i += 1
                    while not lines[i].startswith('}'):
                        k, v = lines[i].split('=', 1)
                        lesson[k.strip()] = v.strip().strip('"')
                        i += 1
                    lessons.append(lesson)
                i += 1

            result['lessons'] = lessons

        i += 1

    return result

def to_xml(data):
    lines = []
    lines.append("<schedule>")
    lines.append(f"  <day>{data['day']}</day>")
    lines.append("  <lessons>")

    for lesson in data['lessons']:
        lines.append("    <lesson>")
        for key, value in lesson.items():
            lines.append(f"      <{key}>{value}</{key}>")
        lines.append("    </lesson>")

    lines.append("  </lessons>")
    lines.append("</schedule>")

    return "\n".join(lines)

# === ОСНОВНАЯ ЧАСТЬ ===
with open("schedule.hcl", "r", encoding="utf-8") as f:
    text = f.read()

data = parse_hcl(text)
xml_text = to_xml(data)

with open("schedule.xml", "w", encoding="utf-8") as f:
    f.write(xml_text)

print(xml_text)