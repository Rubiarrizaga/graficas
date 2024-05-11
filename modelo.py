import matplotlib.pyplot as plt

def calcular_triangulo_w(lamb, t_barra, t_subrayado):
    numerador = lamb * t_subrayado * (t_barra - t_subrayado)
    denominador = lamb * t_subrayado + (1 - lamb) * t_barra
    triangulo_w = numerador / denominador
    return triangulo_w

# Valores fijos
t_subrayado_valor = 5

# Rango de valores para t_barra y lambda
t_barra_valores = range(1, 21)  # Suponiendo valores de 1 a 20 para t_barra
lambda_valores = [i / 10 for i in range(1, 10)]  # Valores de 0.1 a 0.9 para lambda

# Graficar la función manteniendo lambda fijo y variando t_barra
lambda_fijo = 0.5
resultados_t_barra_fijo = [calcular_triangulo_w(lambda_fijo, t, t_subrayado_valor) for t in t_barra_valores]
plt.plot(t_barra_valores, resultados_t_barra_fijo, label=f'lambda={lambda_fijo}')

# Graficar la función manteniendo t_barra fijo y variando lambda
t_barra_fijo = 10
resultados_lambda_fijo = [calcular_triangulo_w(l, t_barra_fijo, t_subrayado_valor) for l in lambda_valores]
plt.plot(lambda_valores, resultados_lambda_fijo, label=f't_barra={t_barra_fijo}')

# Configurar el gráfico
plt.title('Gráfico de la función triangular en función de t_barra y lambda')
plt.xlabel('Valor')
plt.ylabel('Resultado de la función')
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
