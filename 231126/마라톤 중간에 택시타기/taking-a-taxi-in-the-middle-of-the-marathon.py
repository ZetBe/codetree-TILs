n = int(input())
m = [list(map(int, input().split())) for i in range(n)]
a = [0 for i in range(n)]
full = 0
now_y, now_x = m[0][0], m[0][1]
aa = 10**100
for i in range(1, n):
    full += abs(m[i][0]-now_y)+abs(m[i][1]-now_x)
    now_y, now_x = m[i][0], m[i][1]
    if i < n-1:
        temp = abs(abs(now_y-m[i-1][0])+abs(now_x-m[i-1][1]))+abs(abs(now_y-m[i+1][0])+abs(now_x-m[i+1][1]))
        a[i] = temp-(abs(m[i+1][0]-m[i-1][0])+abs(m[i+1][1]-m[i-1][1]))
print(full-max(a))