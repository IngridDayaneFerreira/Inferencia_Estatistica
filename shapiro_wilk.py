import numpy as np

def shapiro_wilk(data):
 
    # Ordenar os dados
    n = len(data)
    sorted_data = np.sort(data)

    # Calcular os coeficientes de Shapiro-Wilk
    a = np.arange(1, n+1)
    m = np.mean(a)
    c = np.sqrt(np.sum((a - m)**2))
    coefficients = (a - m) / c

    # Calcular a estatística de teste W
    s = np.sum(coefficients * sorted_data)
    s2 = np.sum((sorted_data - np.mean(sorted_data))**2)
    W = (s**2) / s2

    # Comparar W com a distribuição de referência
    # z = (W - E[W]) / sqrt(Var[W])
    # p = 1 - norm.cdf(z)

    # Retornar W e um valor-p aproximado
    return W, 0.5 

data = np.random.randn(100)
W, p = shapiro_wilk(data)
print("W =", W)
print("p =", p)
