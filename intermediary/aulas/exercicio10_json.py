import json


def save_json(attr: dict) -> None:
    with open("./class.json", 'w', encoding="utf-8") as atributos:
        json.dump(
            attr,
            atributos,
            indent=2,
            ensure_ascii=False
        )


def load_attr():
    with open("./class.json", 'r', encoding="utf-8") as atributos:
        attr = json.load(atributos)

    return attr
