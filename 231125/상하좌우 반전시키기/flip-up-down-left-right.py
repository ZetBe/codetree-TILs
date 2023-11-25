n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
a = 0
aa = 0

for i in range(1, n-1):
    for j in range(n):
        if j == 0 and arr[i-1][j] == 0:
            aa += 1
            arr[i-1][j], arr[i][j], arr[i+1][j], arr[i][j+1] = (arr[i-1][j]+1)%2, (arr[i][j]+1)%2, (arr[i+1][j]+1)%2, (arr[i][j+1]+1)%2
        elif 0 < j < n-1 and arr[i-1][j] == 0:
            aa += 1
            arr[i-1][j], arr[i][j], arr[i+1][j], arr[i][j+1], arr[i][j-1] = (arr[i-1][j]+1)%2, (arr[i][j]+1)%2, (arr[i+1][j]+1)%2, (arr[i][j+1]+1)%2, (arr[i][j-1]+1)%2
        elif j == n-1 and arr[i-1][j] == 0:
            aa += 1
            arr[i-1][j], arr[i][j], arr[i+1][j], arr[i][j-1] = (arr[i-1][j]+1)%2, (arr[i][j]+1)%2, (arr[i+1][j]+1)%2, (arr[i][j-1]+1)%2
for j in range(n):
    if j == 0 and arr[n-2][j] == 0:
        aa += 1
        arr[n-1][j], arr[n-2][j], arr[n-1][j+1] = (arr[n-1][j]+1)%2, (arr[n-2][j]+1)%2, (arr[n-1][j+1]+1)%2
    elif 0 < j < n-1 and arr[n-2][j] == 0:
        aa += 1
        arr[n-1][j], arr[n-2][j], arr[n-1][j+1], arr[n-1][j-1] = (arr[n-1][j]+1)%2, (arr[n-2][j]+1)%2, (arr[n-1][j+1]+1)%2, (arr[n-1][j-1]+1)%2
    elif j == n-1 and arr[n-2][j] == 0:
        aa += 1
        arr[n-1][j], arr[n-2][j], arr[n-1][j-1] = (arr[n-1][j]+1)%2, (arr[n-2][j]+1)%2, (arr[n-1][j-1]+1)%2

for i in range(n):
    a += sum(arr[i])
if a != n**2:
    print(-1)
else:
    print(aa)