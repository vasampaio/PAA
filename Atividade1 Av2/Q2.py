import numpy as np
# Calcula a probabilidade de k ocorrencias de n eventos
def cal(p,n,k):
    dp = np.zeros((n+1,k+1)) # matriz de probabilidades
    dp[0][0] = 1

    for i in range(1,n+1):
        for j in range(k+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] * (1-p[i]) 
            else:
                dp[i][j] = dp[i-1][j] * (1-p[i]) + dp[i-1][j-1] * p[i]
    return dp[n][k] 

def main():
    p = [0,0.5,0.5] # vetor de probabilidades
    n = 2 # numero de eventos
    k = 1 # numero de ocorrencias
    ans = cal(p,n,k)
    print(ans)

if __name__ == '__main__':
    main()