def multiplicador(opc):
    def x(num):
        return num*opc
    return x


num = input("escolha um número: ").strip().replace(',', '.')
while num.isalpha() or num.isspace() or num in '':
    num = input("escolha um número: ").strip().replace(',', '.')

x2 = multiplicador(2)
x3 = multiplicador(3)
x4 = multiplicador(4)

print(f"O dobro de {float(num)} é {x2(float(num))}, o triplo é {x3(float(num))} e o uadruplo, {x4(float(num))}")
