from math import pi, cos

__all__ = ['rastrigin', 'X_INF', 'X_SUP']

X_INF_Ras = -5.12
X_SUP_Ras = 5.12


def Rastrigin(xi):
    """
    Calcula o valor da função Rastrigin para um x[i]
    
    Parâmetros:
    xi  (float): O valor atual da dimensão
    
    Retorna:
    float: O valor calculado para aquele par de dimensões
    """
    return ((xi**2) - 10*cos(2*pi*xi))

"""
Calcula o valor de rastrigin para as X dimensões

Parâmetro:
x (list[float]): Vetor de valores de len(x) dimensões

Retorna:
float: O valor da função para o conjunto de pontos X[i]
"""
rastrigin = lambda x: 10 * len(x) + sum( Rastrigin(x[i]) for i in range(0, len(x)) )