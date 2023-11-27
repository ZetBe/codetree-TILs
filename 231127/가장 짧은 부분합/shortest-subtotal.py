import sys
n, s = map(int, input().split())
arr = [0] + list(map(int, input().split()))

a = sys.maxsize

j = 0
temp = 0
for i in range(1, n+1):
    
    while j < n and temp+arr[j+1] < s:
        temp += arr[j]
        j += 1
    if temp >= s:
        a = min(a, j-i)
    temp -= arr[i]
if a == sys.maxsize:
    print(-1)
else:
    print(a)