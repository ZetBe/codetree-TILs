s = input()
a1, a2 = 0, 0
for i in range(len(s)-1):
    now = s[i:i+2]
    if now[0] == now[1] == '(':
        a1 += 1
    if now[0] == now[1] == ')':
        a2 += a1
print(a2)