def vowels_count(n):
    dp = [[i for i in range(5,0,-1)] for _ in range(n)]



    for j in range(1,n):
        for k in range(3,-1,-1):
            dp[j][k] = dp[j-1][k] + dp[j][k+1]
            print(dp)
         
    return dp[j][0]

x = vowels_count(3) 
print(x)

