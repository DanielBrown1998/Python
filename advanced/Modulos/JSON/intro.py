import json

string = {
    "Daniel": 25,
    "Rafaela": 25,
    "Rafael": 22,
    "Marcelo": 52,
    "Dayse": 48
    }


with open('name.json', 'w', encoding="utf-8") as file:
    json.dump(string, file, ensure_ascii=False, indent=2)

with open("name.json", 'r', encoding='utf-8') as file:
    dicio: dict = json.load(file)

for k, v in dicio.items():
    print(f"{k}:{v}")
