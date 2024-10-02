import numpy as np
from scipy.stats import norm  # Usaremos a scipy apenas para a CDF da normal

def kolmogorov_smirnov(data, dist='norm', args=()):
   
    n = len(data)
    data_sorted = np.sort(data)

    # Função de distribuição cumulativa empírica
    cdf_emp = np.arange(1, n+1) / n

    # Função de distribuição cumulativa teórica
    cdf_theo = norm.cdf(data_sorted, *args)  # Para a distribuição normal

    # Calcular a estatística de teste D
    D = np.max(np.abs(cdf_emp - cdf_theo))

    # Cálculo aproximado do valor-p para grandes amostras
    z = np.sqrt(n) * D
    p_value = 2 * norm.sf(z)

    return D, p_value

data = np.random.randn(100)
D, p_value = kolmogorov_smirnov(data)
print("D =", D)
print("p-value =", p_value)