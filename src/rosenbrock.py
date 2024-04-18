

__all__ = ['rosenbrock', 'X_INF', 'X_SUP']

X_INF_Ros = -2.048
X_SUP_Ros = 2.048


def Rosenbrock(xi1, xi):
    """
    Calcula o valor da função Rosenbrock para um par de valores X[i] e X[i+1]
    
    Parâmetros:
    xi1 (float): O próximo valor da dimensão
    xi  (float): O valor atual da dimensão
    
    Retorna:
    float: O valor calculado para aquele par de dimensões
    """
    return 100 * ((xi1 - xi**2)**2) + (1 - xi)**2

"""
Calcula o valor de Rosenbrock para as X dimensões

Parâmetro:
x (list[float]): Vetor de valores de len(x) dimensões

Retorna:
float: O valor da função para o conjunto de pontos X[i]
"""
rosenbrock = lambda x: sum( Rosenbrock(x[i+1], x[i]) for i in range(0, len(x)-1) )


