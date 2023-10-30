import json


class AboutMe:
    attribute = None

    def __init__(self, name, curse, age):
        self.name_class = name
        self.objetive = curse
        self.age_class = age


# iniciando a classe
c = AboutMe('Daniel', 'Computation of Science', 25)

# salvando seus atributos
with open('meus_dados.json', 'w', encoding='utf-8') as file:
    json.dump(c.__dict__, file)


