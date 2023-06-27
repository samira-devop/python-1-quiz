def max_values(nums):
  if not nums:  
    return None

  max_val = nums[0]

  for num in nums:
    if num > max_val:
      max_val = num
      max_index = nums.index(max(nums))
  return max_index


# print(max_values([4, 7, 2, 8, 10, 9])) # -> [4, 5]
# print(max_values([-5, -2, -1, -11])) # -> [1, 2]