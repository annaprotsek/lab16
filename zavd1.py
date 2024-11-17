import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, 12, 500)  
y = 2 / np.sqrt(x) + np.cbrt(x) + 1.1

plt.plot(x, y, color='blue', linestyle='-')  
plt.title('Графік функції y = 2/√x + ³√x + 1.1')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.savefig('grafik.png') 
plt.show()
