# Q21. HackerRank Style — No Built-ins

print("\n" + "=" * 50)
print("Q21. HackerRank Style — Without Built-in Functions")
print("=" * 50)

nums = [10, 20, 30, 40, 50]
print("Original list:", nums)

# Maximum without max()
maximum = nums[0]
for n in nums:
    if n > maximum:
        maximum = n
print("Maximum      :", maximum)

# Minimum without min()
minimum = nums[0]
for n in nums:
    if n < minimum:
        minimum = n
print("Minimum      :", minimum)

# Reverse without reverse() or reversed()
reversed_list = []
for i in range(len(nums) - 1, -1, -1):
    reversed_list.append(nums[i])
print("Reversed list:", reversed_list)

print("\n" + "=" * 50)
print("All questions completed successfully!")
print("=" * 50)