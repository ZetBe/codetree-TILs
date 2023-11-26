n = int(input())
line = [list(map(int, input().split())) for i in range(n)]
line.sort()
mb = line[0][1]
a = 1
for i in range(1, n):
    now = line[i][0]
    if now > mb:
        a += 1
        mb = line[i][1]
    elif mb < line[i][1]:
        mb = line[i][1]
    
print(a)