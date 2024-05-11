import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# from google.colab import files
# files.upload()

df = pd.read_csv(r'text')

# para gráficos em linhas
plt.subplot(3, 2, 1) #diz onde o gráfico vai ficar
plt.title('linhas')
# plt.xlabel('taxa')
# plt.ylabel('quant.')
# plt.legend(loc=1) # conectado com os atributos do plt.bar()
plt.plot(df['x'], df['y'], linestyle='dashed', color='blue', label='linha')

# para gráficos em barras
plt.subplot(3, 2, 2)
plt.title('barras verticais')
# plt.xlabel('taxa')
# plt.ylabel('quant.')
# plt.legend(loc=1) # conectado com os atributos do plt.bar()
plt.bar(df['x'], df['y'], color='red', label='barra')

# parra gráficos de pontos
plt.subplot(3, 2, 3)
plt.title('ponto')
# plt.xlabel('taxa')
# plt.ylabel('quant.')
# plt.legend(loc=1) # conectado com os atributos do plt.bar()
plt.scatter(df['x'], df['y'], color='black', label='ponto', marker='D', s=100)
# s: tamanho do ponto
# maker: tipo de ponto

# para gráficos de pizza
x = ['Paulo', 'Daniel', 'Rodri', 'Miguel', 'Rafael']
y = [1, 2, 2, 3, 2]
fatia = [0, 0.4, 0, 0, 0.1]
plt.subplot(3, 2, 4)
plt.title('pizza')
# plt.xlabel('taxa')
# plt.ylabel('quant.')
# plt.legend(loc=1) # conectado com os atributos do plt.bar()
plt.axis('equal') #permite que o gráfico fique redondo
plt.pie(y, labels=x, autopct='%1.1f%%', startangle=90, shadow=True, explode=fatia)
# autopc: formatação

plt.subplot(3, 2, 5)
plt.title('gráficos horizontais')
# plt.xlabel('taxa')
# plt.ylabel('quant.')
# plt.legend(loc=1) # conectado com os atributos do plt.bar()
plt.barh(df['x'], df['y'], color='violet', label='barra')

#descreve o gráfico por completo
print(df.describe())

plt.grid(axis='x')
# põe uma grade no gráfico
# axis define o eixo, pode ser x ou y

plt.show()
