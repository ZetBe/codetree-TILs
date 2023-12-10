s = int(input())
l, r = 1, s
an = 0
while l <= r:
    mid = (l+r)//2
    a = mid*(mid+1)//2
    if a <= s:
        l = mid+1
        an = max(an, mid)
    else:
        r = mid-1
print(an)