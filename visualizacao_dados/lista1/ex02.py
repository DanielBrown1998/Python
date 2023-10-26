import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r'../Iris/iris.data')

sepallength = df['sepallength']
sepalwidth = df['sepalwidth']
petallength = df['petallength']
petalwidth = df['petalwidth']
opc = df['class']
labels = dict()
tipos = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
fatia = list()
x, y, z = 0, 0, 0
for c in range(150):
    labels[opc[c]] = sepallength[c]

for k, v in labels.items():
    if k == tipos[0]:
        x += 1
    elif k == tipos[1]:
        y += 1
    else:
        z += 1
fatia.append(x)
fatia.append(y)
fatia.append(z)

plt.title('pizzaaahh!!!')
plt.axis('equal')
plt.pie(fatia, labels=tipos)
plt.show()
# Os valores serão congruentes para quaisquer argumentos
