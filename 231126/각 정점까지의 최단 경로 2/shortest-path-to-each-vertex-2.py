import sys
INT_MAX = sys.maxsize

n, m = map(int, input().split())
dp = [[INT_MAX for j in range(n)] for i in range(n)]
for i in range(m):
    t, f, g = map(int, input().split())
    dp[t-1][f-1] = min(dp[t-1][f-1], g)

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
for i in range(n):
    for j in range(n):
        if dp[i][j] == INT_MAX:
            dp[i][j] = -1
        if i == j:
            dp[i][j] = 0
for i in dp:
    print(*i)