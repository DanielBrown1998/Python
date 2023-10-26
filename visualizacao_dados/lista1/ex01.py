import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../Iris/iris.data')

plt.title('gráfico questão 1')
plt.xlabel('sepallength ou sepallwidth')
plt.ylabel('petallength ou petalwidth')

plt.plot(df['sepallength'], df['petallength'], label='petalXsepal(length)', color='red')
plt.legend(loc=2)
plt.show()

plt.bar(df['sepallength'], df['petalwidth'], label='sepallengthXpetalwidth', color='blue')
plt.legend(loc=2)
plt.show()


plt.scatter(df['sepalwidth'], df['petalwidth'], label='sepalXpetal(width)', color='black')
plt.legend(loc=2)
plt.show()


try:
    plt.axis('equal')
    fatia = list()
    tipos = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    x, y, z = 0, 0, 0
    for c in df['class']:
        if c == 'Iris-setosa':
            x += 1
        elif c == 'Iris-versicolor':
            y += 1
        elif c == 'Iris-virginica':
            z += 1
    fatia.append(x)
    fatia.append(y)
    fatia.append(z)
    if len(fatia) == len(tipos):
        plt.pie(fatia, labels=tipos, shadow=True)
except Exception as erro:
    print(f'ocorreu um erro: {erro.__cause__}')
plt.show()
