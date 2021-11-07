def fibonacci(n):
    dp = [] 
    dp.append(0) 
    dp.append(1)
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])   
    return dp[n]

def main():
    n = int(input())
    print(fibonacci(n))

if __name__ == "__main__":
    main()
