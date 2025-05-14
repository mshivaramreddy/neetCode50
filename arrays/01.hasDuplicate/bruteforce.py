from typing import List

def hasDuplicate(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

nums = [1,3,4,8,2]
result = hasDuplicate(nums)
print(result)


# Time C
# Space C