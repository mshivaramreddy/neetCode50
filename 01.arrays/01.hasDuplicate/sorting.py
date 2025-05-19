from typing import List

def hasDuplicate(nums: List[int]) -> bool:
    sorted(nums)

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            return True
    return False

nums = [1,3,4,8,2]
result = hasDuplicate(nums)
print(result)

# Time C
# Space C