n, m = map(int, input().split())
arr = list(map(int, input().split()))
dp = [[0 for i in range(41)] for j in range(n)]

dp[0][arr[0]+20] += 1
dp[0][-arr[0]+20] += 1
for i in range(1, n):
    for j in range(41):
        if dp[i-1][j] > 0:
            if j-arr[i] >= 0:
                dp[i][j-arr[i]] += dp[i-1][j]
            if j+arr[i] <= 40:
                dp[i][j+arr[i]] += dp[i-1][j]
print(dp[n-1][m+20])