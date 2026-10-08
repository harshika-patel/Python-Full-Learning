# List Comprehensions
# [output for item in iterable if condition]
sqaure = []
for i in range(6):
    sqaure.append(i*i)
print(sqaure)

sqaures = [i*i for i in range(7) if i % 2 != 0]
print(sqaures)

nums = [-2, -4, 3, 5, -2, 0, -1, 2]
print(nums)
nums = [0 if val < 0 else val for val in nums]

print(nums)
