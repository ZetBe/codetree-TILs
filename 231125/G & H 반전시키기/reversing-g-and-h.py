n = int(input())
a = list(input())
b = list(input())
g = [0 for i in range(n)]
aa = 0

for i in range(n):
    if a[i] != b[i]:
        g[i] += 1

for i in range(n-1):
    if g[i] == 1 and g[i+1] == 0:
        aa += 1
if g[n-1] == 1:
    aa += 1
print(aa)