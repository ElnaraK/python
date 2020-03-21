n = int(input())
nums = []
s = 0
for i in range (0, n):
    number = int(input())
    nums.append(number)
    s = s+number
print(s)