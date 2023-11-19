n = int(input())
arr = [list(map(int, input().split())) for i in range(4)]
for i in range(4):
    arr[i].sort()
d = {}
ans = 0
for i in range(n):
    for j in range(n):
        now = (arr[0][i] + arr[1][j])*-1
        if now in d:
            d[now] += 1
        else:
            d[now] = 1
for i in range(n):
    for j in range(n):
        now = arr[2][i] + arr[3][j]
        if now in d:
            ans += d[now]
print(ans)