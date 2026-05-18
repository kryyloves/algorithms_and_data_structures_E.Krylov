nums = [10, 9, 2, 5, 3, 7, 101, 18, 1]

n = len(nums)
dp = [1] * n

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1

max_length = 0
for x in dp:
    if x > max_length:
        max_length = x

print(max_length)