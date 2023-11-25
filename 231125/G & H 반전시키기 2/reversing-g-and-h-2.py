n = int(input())
a = input()
b = input()
g = [0 for i in range(n)]
an = 0
for i in range(n):
    if a[i] != b[i]:
        g[i] += 1

for i in range(n):
    if g[n-i-1] == 1:
        for j in range(n-i):
            g[j] = (g[j]+1)%2
        an += 1
print(an)