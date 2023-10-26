import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

# n° de acessos
lista = list()
for c in range(1, 101):
    lista.append(c)

# retenção dos clientes
clientes = list()
for i in lista:
    if i <= 10:
        clientes.append(i*0.4)
    elif 20 <= i <= 25:
        clientes.append(i*0.3)
    elif 30 <= i <= 70:
        clientes.append(i*0.1)
    elif 80 <= i <= 100:
        clientes.append(i*0.5)
    else:
        clientes.append(i*0.2)
# pré configuração
plt.rcParams.update({'font.size': 16})
plt.figure(figsize=(8, 5))
#gerando o gráfico
plt.plot(clientes, color='crimson')
# customizando o gráfico
plt.title('Performance', fontsize=20, fontweight='bold', fontstyle='italic')
plt.xlabel('tempo (month)', fontsize=14)
plt.ylabel('taxa de retenção (%)', fontsize=14)
# ajustando o gráfico
plt.xlim([0, 101])
plt.ylim([0, 101])
# mostrando o gráfico
plt.savefig('aula01.1.jpg', dpi=600, transparent=True)
plt.show()
# salvando o gráfico

# exercício do aula do dia 03/04/2023
