n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
c = 0
l, r = 0, n-1
while l != r:
    if arr[l] + arr[r] == k:
        l += 1
        c += 1
    elif arr[l] + arr[r] > k:
        r -= 1
    else:
        l += 1
print(c)