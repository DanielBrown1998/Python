import matplotlib.pyplot as plt
import numpy as np


x_max, y_max = 4000, 4000

x, y = np.linspace(0, x_max, 400), np.linspace(0, y_max, 400)

#3x + 2y <= 6000

y1 = (6000 -3*x)/2
y2 = (5500 -2*x)/3
y3 = 10*x


plt.figure(figsize=(10,8))

plt.fill_between(x,0, np.minimum(np.minimum(y1, y2), y3), where=(y1>=0)&(y2>=0)&(y3>=0), color='b', alpha=.3)

plt.plot(x, y1, color='b', label='Restrição de água')
plt.plot(x, y2, color='g', label='Restrição de espaço')
plt.plot(x, y3, color='r', label='Restrição de diversificação')

X, Y = np.meshgrid(x,y)

Z = 2*X + 1.5*Y

plt.contour(X, Y, Z, alpha=.5, cmap='jet')

plt.xlim(0, x_max)
plt.ylim(0, y_max)

plt.xlabel("Quantidade de tomates em Kg")
plt.ylabel("Quantidade de alfaces em Kg")


plt.legend()
plt.show()
