import sys
n = int(input())
arr = list(map(int, input().split()))

now = 0
a = 0
answer = -sys.maxsize
for now in range(n):
    if a + arr[now] < 0 or a < 0:
        a = 0
    a += arr[now]
    answer = max(a, answer)
print(answer)