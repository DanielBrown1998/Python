import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r'../Iris/iris.data')


def args(title,x='',y=''):
    plt.title(str(title))
    plt.xlabel(str(x))
    plt.ylabel(str(y))


plt.subplot(2, 2, 1)
args('linhas', x='sepallength', y='petallength')
plt.plot(df['sepallength'], df['petallength'], label='petalXsepal(length)', color='red')

plt.subplot(2, 2, 2)
args('linhas', x='seplalength', y='petalwidth')
plt.bar(df['sepallength'], df['petalwidth'], label='sepallengthXpetalwidth', color='blue')

plt.subplot(2, 2, 3)
args('linhas', x='sepalwidth', y='petalwidth')
plt.scatter(df['sepalwidth'], df['petalwidth'], label='sepalXpetal(width)', color='black')

plt.subplot(2, 2, 4)

try:
    plt.axis('equal')
    args('pizza')
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
        plt.pie(fatia, labels=tipos, autopct='%1.1f%%', shadow=True)
except Exception as erro:
    print(f'ocorreu um erro: {erro.__cause__}')

plt.show()
