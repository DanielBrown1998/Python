import re

# metacaracteres: ^$ ()

texto = """
<p>frase 1</p> <p>frase 2</p> <p>qualquer coisa</p> <div></div>
"""

# greedy (guloso)
print(re.findall(r'<[dpiv]{1,3}>.*</[dpiv]{1,3}>', texto, flags=re.I))

# non-greedy (não guloso) (lazy)
print(re.findall(r'<[dpiv]{1,3}>.*?</[dpiv]{1,3}>', texto, flags=re.I))
