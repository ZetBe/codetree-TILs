n = int(input())
l, r = 1, n*2

while l <= r:
    mid = (l+r)//2
    if mid%3==0 or mid%5==0:
        r+=2
    else:
        three = mid//3
        five = mid//5
        tf = mid//15
        total = mid-(three+five-tf)
        if total == n:
            break
        elif total < n:
            l = mid+1
        else:
            r = mid-1
print(mid)