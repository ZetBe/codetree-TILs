n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
p = [1 for i in range(n-1)]

for i in edges:
    if i[1]-2 >= 0:
        p[i[1]-2] = i[0]
for i in p:
    print(i)