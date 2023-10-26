import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(0, 100, 10000)
y = [math.sqrt(c) for c in x]
z = x**3
plt.plot(x, y, 'g', label='raiz quadrada')
plt.plot(x, z, 'r', label='ao cubo')
plt.xlabel('eixo X', fontsize=16, fontstyle='italic')
plt.ylabel('eixo Y', fontsize=16, fontstyle='italic')
plt.title('Segundo Gráfico', fontsize=18, fontstyle='italic', fontweight='bold')
plt.xlim([0, 5])
plt.ylim([0, 5])
plt.savefig('aula02.png', dpi=600, transparent=True)
plt.legend(loc=1)
plt.show()
