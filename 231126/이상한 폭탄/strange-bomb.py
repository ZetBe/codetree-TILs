n, k = map(int, input().split())
d = {}
a = 0
for i in range(n):
    now = int(input())
    if now not in d:
        d[now] = i
    else:
        if d[now] + k >= i:
            a = max(a, now)
print(a)