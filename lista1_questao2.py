import numpy as np
import matplotlib.pyplot as plt


y0 = 0
const_a = 8
const_b = 12
t = np.linspace(0, 1, 100)
y_values = []

for y0 in range(-10,30,3):
    y = np.zeros(len(t))

    for i in range(len(t)):
        y[i] = (y0 + const_b/const_a) * np.exp(const_a*t[i]) - const_b/const_b
    y_values.append(y)
for i in range(len(y_values)):
    plt.plot(t,y_values[i])
plt.show()

'''
# Use um loop for para calcular e armazenar os valores de y em cada iteração
for i in range(len(t)):
    y[i] = (y0 + const_b / const_a) * (math.exp(const_a * t[i])) - const_b / const_a

plt.plot(t,y)
plt.show()
'''
