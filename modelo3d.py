import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def calcular_Wage_gap(lamb, t_barra, t_subrayado):
    numerador = lamb * t_subrayado * (t_barra - t_subrayado)
    denominador = lamb * t_subrayado + (1 - lamb) * t_barra
    Wage_gap = numerador / denominador
    return Wage_gap

# Valores fijos
t_subrayado_valor = 15

# Rangos de valores para t_barra y lambda
t_barra_valores = np.arange(1, 21, 1)  # Suponiendo valores de 1 a 20 para t_barra
lambda_valores = np.arange(0.1, 1, 0.1)  # Valores de 0.1 a 0.9 para lambda

# Crear una cuadrícula de valores para t_barra y lambda
T_barra, Lambda = np.meshgrid(t_barra_valores, lambda_valores)

# Calcular los resultados de la función para cada combinación de valores
resultados = calcular_Wage_gap(Lambda, T_barra, t_subrayado_valor)

# Graficar en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(T_barra, Lambda, resultados, cmap='viridis')

# Configurar etiquetas y título
ax.set_xlabel('Transportation Costs')
ax.set_ylabel('$\lambda$')
ax.set_zlabel('Wage Gap')
#plt.title('Three-dimensional Graph of Salary Differential')

# Mostrar el gráfico
plt.show()
