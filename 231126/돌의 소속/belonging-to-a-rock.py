n, q = map(int, input().split())
stone = [[0, 0, 0] for i in range(n+1)]
for i in range(1, n+1):
    stone[i] = stone[i-1][:]
    s = int(input())
    stone[i][s-1] += 1

for i in range(q):
    a, b = map(int, input().split())
    now = [0, 0, 0]
    for i in range(3):
        now[i] = stone[b][i]-stone[a-1][i]
    print(*now)