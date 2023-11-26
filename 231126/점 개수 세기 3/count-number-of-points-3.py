from sortedcontainers import SortedSet

n, q = map(int, input().split())
arr = list(map(int, input().split()))
edges = [list(map(int, input().split())) for i in range(q)]
arr.sort()
nums = SortedSet()
for i in arr:
    nums.add(i)
mapper = {}
cnt = 1
for num in nums:
    mapper[num] = cnt
    cnt += 1
for a, b in edges:
    a, b = mapper[a], mapper[b]
    print(b-a+1)