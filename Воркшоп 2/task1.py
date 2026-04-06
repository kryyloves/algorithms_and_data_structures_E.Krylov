s = input()
left = 0
max_len = 0
chars = set()

for right in range(len(s)):
    while s[right] in chars:
        chars.remove(s[left])
        left += 1
    chars.add(s[right])
    max_len = max(max_len, right - left + 1)

print(max_len)