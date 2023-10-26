
with open('file.txt', 'w+', encoding='utf-8') as file:
    print('abrindo a pasta')
    c = 0
    while c < 3:
        word = str(input('digite algo: '))
        file.write(f"{word}\n")
        c += 1
print("pasta fechada")

with open('file.txt', 'r') as file:
    print(file.read())
