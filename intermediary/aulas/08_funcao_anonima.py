lista = [
    {
        "nome": "João",
        "idade": 25
    },
    {
        "nome": "Maria",
        "idade": 30
    },
    {
        "nome": "José",
        "idade": 20
    },
    {
        "nome": "Pedro",
        "idade": 35
    }
]
list_ordered = sorted(
    lista,
    key=lambda x: x["idade"]
)
print(list_ordered)
# Output: [{'nome': 'José', 'idade': 20}, {'nome': 'João', 'idade': 25}, {'nome': 'Maria', 'idade': 30}, {'nome': 'Pedro', 'idade': 35}]