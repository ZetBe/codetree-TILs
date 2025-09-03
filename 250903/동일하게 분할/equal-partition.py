n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
dp = [0 for i in range(sum(arr)+1)]
for i in arr:
    dp[i] = 1
for i in range(sum(arr)):
    for j in arr:
        if i+j < n:
            dp[i+j] = 1
if dp[sum(arr)//2] == 1:
    print('Yes')
else:
    print('No')