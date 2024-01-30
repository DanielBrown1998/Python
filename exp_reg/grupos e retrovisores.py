import re

# metacaracteres: ^ $
# [abc] -> 'a' ou 'b' ou 'c'
# (abc) -> abc
# (def|abc)-> def ou abc

texto = """
<p>frase 1</p> <p>frase 2</p> <p>qualquer coisa</p> <div></div>
"""
# print(re.findall(r'<[dpiv]{1,3}>.*</[dpiv]{1,3}>', texto, flags=re.I))
print(re.findall(r'(<([dpiv]{1,3})>.*?</\2>)', texto, flags=re.I))

