n, k = map(int, input().split())
arr = list(map(int, input().split()))
a = -10**100
now = sum(arr[:k])
if now > a:
    a = now
for i in range(n-k):
    now -= arr[i]
    now += arr[i+k]
    if now > a:
        a = now
print(a)