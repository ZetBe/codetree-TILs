n, m = map(int, input().split())
arr = [int(input()) for i in range(n)]
l, r = 0, max(arr)
a = 0
while l <= r:
    mid = (l+r)//2
    count = 0
    for i in arr:
        c = i//mid
        count += c
    if count == m:
        l += 2
        a = max(a, mid)
    elif count < m:
        r = mid - 1
    else:
        l = mid + 1
print(a)