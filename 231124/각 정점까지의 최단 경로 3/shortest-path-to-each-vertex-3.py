n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
dijk = [-1 for i in range(n+1)]
v = [0 for i in range(n+1)]
for i in range(m):
    t, f, g = map(int, input().split())
    graph[t].append([f, g])
def dijkstra(n, now):
    if dijk[n] == -1:
        dijk[n] = now
    else:
        dijk[n] = min(now, dijk[n])
    if v[n] == 1:
        return
    v[n] = 1
    for i in graph[n]:
        dijkstra(i[0], now+i[1])

v[1] = 1
for i in graph[1]:
    dijkstra(i[0], i[1])

if n == 1:
    print(0)
else:
    for i in range(2, len(dijk)):
        print(dijk[i])