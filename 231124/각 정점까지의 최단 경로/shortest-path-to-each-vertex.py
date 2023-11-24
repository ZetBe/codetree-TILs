import heapq
n, m = map(int, input().split())
k = int(input())
hq = []
graph = [[] for j in range(n+1)]
dijk = [10**1000 for i in range(n+1)]
dijk[k] = 0

heapq.heappush(hq, (0, k))

for i in range(m):
    f, t, g = map(int, input().split())
    graph[f].append((t, g))
    graph[t].append((f, g))

while hq:
    min_dist, min_index = heapq.heappop(hq)

    if min_dist != dijk[min_index]:
        continue

    for idx, dist in graph[min_index]:
        new_dist = dijk[min_index] + dist
        if dijk[idx] > new_dist:
            dijk[idx] = new_dist
            heapq.heappush(hq, (new_dist, idx))

for i in range(1, n+1):
    if dijk[i] == 10**1000:
        print(-1)
    else:
        print(dijk[i])