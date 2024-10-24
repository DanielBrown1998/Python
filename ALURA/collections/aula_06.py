
sentence = "Eu vim para a Universidade hoje, para que eu possa passar na matéria"
sentence = sentence.lower().replace(', ', ' ').strip()
sentence = sentence.split()

num_words = len(set(sentence))
word_in_sentence = {}


for word in sentence:
    if word in word_in_sentence.keys():
        word_in_sentence[word] += 1
    else:
        word_in_sentence[word] = 1

print(f'Número de palavras: {num_words}')
print(*word_in_sentence.items())
