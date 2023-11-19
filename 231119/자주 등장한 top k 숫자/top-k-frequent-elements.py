n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

a = {}

for elem in arr:
    if elem in a:
        a[elem] += 1
    else:
        a[elem] = 1
a = sorted(a.items(), key=lambda x:(-x[1], -x[0]))
for i in range(k):
    print(a[i][0], end=' ')