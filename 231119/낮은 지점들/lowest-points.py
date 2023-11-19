n = int(input())

arr = [list(map(int, input().split())) for i in range(n)]
d = {}
for i in range(n):
    if arr[i][0] in d and d[arr[i][0]] > arr[i][1]:
        d[arr[i][0]] = arr[i][1]
    elif arr[i][0] not in d:
        d[arr[i][0]] = arr[i][1]
ans = 0
for k, v in d.items():
    ans += v
print(ans)