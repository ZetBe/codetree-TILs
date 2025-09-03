n = int(input())
arr = list(map(int, input().split()))
arr.sort()
# Please write your code here.
dp = [[] for i in range(sum(arr)+1)]
for i in range(n):
    if len(dp[arr[i]]) == 0:
        dp[arr[i]].append(i)
for i in range(sum(arr)):
    for j in range(n):
        if i-arr[j] >= 0 and len(dp[i-arr[j]]) > 0 and j not in dp[i-arr[j]]:
            temp = 0
            for k in dp[i]:
                temp += arr[k]
            if temp < i:
                dp[i] = dp[i-arr[j]][:]
                dp[i].append(j)
if sum(arr) % 2 == 1:
    print('No')
else:
    if len(dp[sum(arr)//2]) > 0:
        print('Yes')
    else:
        print('No')