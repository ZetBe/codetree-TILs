import heapq

n, m = map(int, input().split())
dijk = [10**1000 for i in range(n+1)]
dijk[0] = 0
graph = [[] for i in range(n+1)]
for i in range(m):
    t, f, g = map(int, input().split())
    graph[f].append([g, t])
dijk[n] = 0
hq = []

heapq.heappush(hq, (0, n))

while hq:
    min_dist, min_index = heapq.heappop(hq)

    if min_dist != dijk[min_index]:
        continue
    
    for target_dist, target_index in graph[min_index]:
        new_dist = target_dist + dijk[min_index]
        if dijk[target_index] > new_dist:
            dijk[target_index] = new_dist
            heapq.heappush(hq, (new_dist, target_index))

a = 0

for i in dijk:
    if a < i:
        a = i

print(a)