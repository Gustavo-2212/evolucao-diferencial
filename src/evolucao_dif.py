import numpy as np
from math import ceil


def inicializa_geracao(NP, N, X_INF, X_SUP):
    """
    Inicializa o vetor da primeira geração, com valores aleatórios
    
    Parâmetros
    NP (int):       Número de indivíduos na geração, população
    N (int):        Número de dimensões consideradas
    X_INF (float):  Valor mínimo das variáveis independentes
    X_SUP (float):  Valor máximo das variáveis independentes
    
    Retorna
    list(list(float)): Um vetor com os valores iniciais para a primeira geração de indivíduos
    """
    x_inf = np.ones(N) * X_INF
    x_sup = np.ones(N) * X_SUP
        
    return np.random.uniform(x_inf, x_sup, size=(NP, N))


def evolucao(NG=400, NP=15, CrossOver=0.8, N=5, F=0.9, func=None, X_INF=None, X_SUP=None):
    """
    Função para a evolução dos indivíduos
    
    Parâmetros
    NG (int):           Quantidade de gerações
    NP (int):           Quantidade de indivíduos por geração
    CrossOver (float):  Probabilidade de ocorrer o cross-over. Valor entre 0 < CrossOver <= 1
    N (int):            Número de dimensões sendo consideradas
    F (float):          Fator de escala. Valor entre 0 <= F <= 2
    func:               Função para otimizar
    X_SUP/X_INF (float): Valores mínimo e máximo das variáveis independentes
    
    Retorna
    list(list(float)): retorna as gerações com seus indivíduos
    """
    if(not func or not X_INF or not X_SUP):
        print("Coloque a função para ser otimizada!")
        return 
    
    geracao = 0
    vetor_geracao = inicializa_geracao(NP, N, X_INF, X_SUP)
    
    vetor_trial = np.zeros((NP, N))
    fit_trial = np.zeros(NP)
    
    fit_populacao = np.zeros(NP)
    for individuo in range(NP):
        fit_populacao[individuo] = func(vetor_geracao[individuo, :])
    
    while(geracao < NG):
        
        for i in range(NP):
            candidatos = list(range(0, i)) + list(range(i+1,NP))
            np.random.shuffle(candidatos)
            
            X1 = vetor_geracao[candidatos[0]]
            X2 = vetor_geracao[candidatos[1]]
            X3 = vetor_geracao[candidatos[3]]

            mutante = X1 + F * (X3 - X2)

            delta = np.random.randint(0, N)
            for j in range(0, N):
                if((np.random.rand() <= CrossOver) or (delta == j)):
                    vetor_trial[i][j] = mutante[j]
                else:
                    vetor_trial[i][j] = vetor_geracao[i][j]
        
        for j in range(0, NP):
            
            for x in range(0, N):
                vetor_trial[j][x] = min(X_SUP, vetor_trial[j][x])
                vetor_trial[j][x] = max(X_INF, vetor_trial[j][x])
                
            fit_trial[j] = func(vetor_trial[j])
            
            if abs(fit_trial[j]) < abs(fit_populacao[j]):
                vetor_geracao[j] = vetor_trial[j]
                fit_populacao[j] = fit_trial[j]
                    
        geracao += 1
    
    return vetor_geracao, fit_populacao
        
        
__all__ = ['evolucao'] 