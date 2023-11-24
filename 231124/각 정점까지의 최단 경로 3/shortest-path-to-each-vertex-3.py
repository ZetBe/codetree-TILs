n, m = map(int, input().split())
graph = [[0 for j in range(n+1)] for i in range(n+1)]
dijk = [10**1000 for i in range(n+1)]
v = [0 for i in range(n+1)]
for i in range(m):
    t, f, g = map(int, input().split())
    graph[t][f] = g

dijk[1] = 0

for i in range(1, n+1):
    min_index = -1
    for j in range(1, n+1):
        if v[j] == 1:
            continue
        
        if min_index == -1 or dijk[min_index] > dijk[j]:
            min_index = j
    v[min_index] = 1

    for j in range(1, n+1):
        if graph[min_index][j] == 0:
            continue
        
        dijk[j] = min(dijk[j], dijk[min_index]+graph[min_index][j])

for i in range(2, n+1):
    if dijk[i] == 10**1000:
        print(-1)
    else:
        print(dijk[i])