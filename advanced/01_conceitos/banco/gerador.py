agencia = [c for c in range(100)]

with open("agencia.txt", 'w') as file:
    for c in agencia:
        file.write(f"{c}\n")

conta = [c for c in range(1000, 10000)]

with open("conta.txt", 'w') as file:
    for c in conta:
        file.write(f"{c}\n")

