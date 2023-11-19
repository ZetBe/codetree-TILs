n, m = map(int, input().split())
d = dict()
rd = dict()
for i in range(n):
    a = input()
    d[a] = i+1
    rd[i+1] = a
for i in range(m):
    a = input()
    if a in d:
        print(d[a])
    elif int(a) in rd:
        print(rd[int(a)])