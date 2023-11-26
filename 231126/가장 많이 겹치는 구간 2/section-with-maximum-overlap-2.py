import heapq
x1, x2 = [], [] 
n = int(input())
line = [list(map(int, input().split())) for i in range(n)]
line.sort()
for i in range(n):
    heapq.heappush(x1, line[i][0])
    heapq.heappush(x2, line[i][1])
a = 1
answer = 1
heapq.heappop(x1)
for i in range(n*2-1):
    if len(x1) == 0:
        break
    if x1[0] <= x2[0]:
        a += 1
        answer = max(answer, a)
        heapq.heappop(x1)
    else:
        a -= 1
        heapq.heappop(x2)

print(answer)