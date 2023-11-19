n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
d = dict()
ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        now = k-arr[i]-arr[j]
        if now in d:
            ans += d[now]
        
        if arr[i]+arr[j] in d:
            d[arr[i]+arr[j]] += 1
        else:
            d[arr[i]+arr[j]] = 1
print(ans)