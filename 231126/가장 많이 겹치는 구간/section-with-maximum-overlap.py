n = int(input())
m = [0 for i in range(200001)]

for i in range(n):
    a, b = map(int, input().split())
    m[a] += 1
    m[b] -= 1
a = 0
an = 0
for i in m:
    a += i
    if i == 1:
        an = max(a, an)
print(an)