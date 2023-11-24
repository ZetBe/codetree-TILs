n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0 for j in range(m)] for i in range(n)]
dp[0][0] = arr[0]
dp[n-1][m-1] = arr[n-1]
for i in range(1, n):
    dp[i][0] += arr[i]+dp[i-1][0]

for j in range(1, m):
    for i in range(2, n):
        for k in range(i-1):
            dp[i][j] = max(dp[i][j], dp[i-2-k][j-1]+arr[i], dp[i-1][j]+arr[i])

print(dp[n-1][m-1])