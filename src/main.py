from rosenbrock import rosenbrock, X_INF_Ros, X_SUP_Ros
from rastrigin import rastrigin, X_INF_Ras, X_SUP_Ras
from evolucao_dif import evolucao


def main():
    ultima_geracao_ros, fit_ros = evolucao(NG=700, N=7, func=rosenbrock, X_INF=X_INF_Ros, X_SUP=X_SUP_Ros)
    
    print("="*90, "\n\tROSENBROCK\n")
    for i in range(len(ultima_geracao_ros)):
        print(ultima_geracao_ros[i], '\t==>\t', fit_ros[i], end="\n\n")
        
        
    print("\n\n")
    print("="*90, "\n\tRASTRIGIN\n")
    ultima_geracao_ras, fit_ras = evolucao(NG=150, N=2, func=rastrigin, X_INF=X_INF_Ras, X_SUP=X_SUP_Ras)
    
    for i in range(len(ultima_geracao_ras)):
        print(ultima_geracao_ras[i], '\t==>\t', fit_ras[i])
    
if __name__ == '__main__':
    main()