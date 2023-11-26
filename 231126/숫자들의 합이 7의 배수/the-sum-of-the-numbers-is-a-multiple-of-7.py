n = int(input())
a = [0]
temp = 0
d = {}
answer = 0
for i in range(n):
    now = int(input())
    temp += now
    a.append(temp)
    if temp%7 in d:
        answer = max(answer, i-d[temp%7])
    else:
        d[temp%7] = i
print(answer)