import hcl2
import yaml

with open("schedule.hcl", "r", encoding="utf-8") as f:
    data = hcl2.load(f)

with open("schedule_lib.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data, f, allow_unicode=True)

print(data)