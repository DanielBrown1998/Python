import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv(r'../Iris/iris.data')

# ============================================================================

plt.subplot(2, 3, 1)
plt.title('sepalXpetal(length)', fontsize=10)
plt.xlabel('sepallength', fontsize=10)
plt.ylabel('petallength', fontsize=10)
plt.scatter(df['sepallength'], df['petallength'], color='pink')

# ============================================================================
plt.subplot(2, 3, 2)
plt.title('sepalXpetal(width)', fontsize=10)
plt.xlabel('sepalwidth', fontsize=10)
plt.ylabel('petalwidth', fontsize=10)
plt.bar(df['sepalwidth'], df['petalwidth'], color='blue')

plt.subplot(2, 3, 3)
plt.title('sepalXpetal(lengthXwidth)', fontsize=10)
plt.xlabel('sepallength', fontsize=10)
plt.ylabel('petalwidth', fontsize=10)
plt.barh(df['sepallength'], df['petalwidth'], color='green')

# ============================================================================
try:
    plt.subplot(2, 3, 4)
    plt.title('tipos de petalas', fontsize=10)
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
        plt.pie(fatia, labels=tipos, autopct='%1.1f%%', shadow=True)
except Exception as erro:
    print(f'ocorreu um erro: {erro.__cause__}')

# ============================================================================
plt.subplot(2, 3, 5)
plt.title('sepal(lengthXwidth)', fontsize=10)
plt.xlabel('sepalwidth', fontsize=10)
plt.ylabel('sepallength',fontsize=10)
plt.scatter(df['sepalwidth'], df['sepallength'], color='red')

# ============================================================================
plt.show()
