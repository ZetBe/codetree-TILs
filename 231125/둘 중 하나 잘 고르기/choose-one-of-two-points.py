n = int(input())
arr = [list(map(int, input().split())) for i in range(n*2)]
dp = [[0 for i in range(n*2)] for j in range(n*2)]

dp[0][0], dp[0][1] = arr[0][0], arr[0][1]
for i in range(1, n*2):
    for j in range(i+1):
        if j < n*2:
            dp[i][j] = max(dp[i][j], dp[i-1][j]+arr[i][0], dp[i-1][j-1]+arr[i][1])
print(dp[n*2-1][n])