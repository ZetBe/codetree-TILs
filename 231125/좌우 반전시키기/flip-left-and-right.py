n = int(input())
arr = list(map(int, input().split()))
a = 0
for i in range(1, n):
    if arr[i-1] == 0:
        arr[i-1], arr[i], arr[i+1] = (arr[i-1]+1)%2, (arr[i]+1)%2, (arr[i+1]+1)%2
        a += 1
print(a)