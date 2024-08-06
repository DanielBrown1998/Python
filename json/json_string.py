import json
from typing import TypedDict
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie = True
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float


string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''

# Convertendo a string JSON para um dicionário Python
filme: Movie = json.loads(string_json)
print(filme)
# Convertendo um dicionário Python para uma string JSON
filme_json = json.dumps(filme, indent=2, ensure_ascii=False)

print(filme_json)
