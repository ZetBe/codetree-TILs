import bisect
n, q = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in range(q):
    a, b = map(int, input().split())
    print(bisect.bisect_right(arr, b)-bisect.bisect_left(arr, a))