def vowels_count(n):
    """
    input = integer
    This function gets input as an integer n 
    and returns the length of all the possible combination of vowels of size n sorted lexicographically  
    output = length of string
    """
    
    dp = [[i for i in range(5,0,-1)] for _ in range(n)]



    for j in range(1,n):
        for k in range(3,-1,-1):
            dp[j][k] = dp[j-1][k] + dp[j][k+1]
         
    return dp[j][0]

if __name__=="__main__":
    x = vowels_count(3) 
    print(x)

