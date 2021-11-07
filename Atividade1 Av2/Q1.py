# Essa função calcula o custo das paradas em cada hotel
def dist(v):
    dp = []
    n = len(v)
    for i in range(n):
        aux = (200 - v[i])**2 #função de custo
        dp.append(aux)

        for j in range(i):
            calc = dp[j] + (200 -(v[i]-v[j]))**2 
            dp[i] = min(dp[i], calc) 
    
    return dp[n-1]


def main():
    v = [100,200,300] # vetor de custos
    ans = dist(v)
    print(ans)

if __name__ == "__main__":
    main()