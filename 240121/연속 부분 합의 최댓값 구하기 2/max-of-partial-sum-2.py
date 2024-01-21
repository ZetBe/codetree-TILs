n = int(input())
arr = list(map(int, input().split()))

now = 0
a = 0
answer = -100**1000
while now < n:
    if a + arr[now] < 0:
        a = 0
    a += arr[now]
    now += 1
    answer = max(a, answer)
print(answer)