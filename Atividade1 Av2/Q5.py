g = [] #lista de adjacência
visited = [] #lista de visitados
dp = []
def dfs(u): #u é o nó atual
    global dp 
    global visited
    visited[u] = True #marca como visitado
    for v in g[u]:
        if not visited[v]: #se não foi visitado
            dfs(v) #visita o nó v
    dp[u] = max(dp[u], 1+dp[v]) #adiciona 1 ao maior caminho

def longest_path(n): #n é o número de nós
    for i in range(n):
        if not visited[i]: 
            dfs(i)
    return max(dp) #retorna o maior caminho

def main():
    n = 4 #número de nós
    global g
    g = [[0,1],[1,3],[2,3],[0,2],[2,1]] #lista de adjacência
    global visited
    visited = [False] * n #lista de visitados do tamanho de n
    global dp
    dp = [0] * n #lista de maior caminho do tamanho de n
    print(longest_path(n))

if __name__ == '__main__':
    main()
