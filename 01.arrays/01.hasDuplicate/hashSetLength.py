from typing import List

def hasDuplicate(nums: List[int]) -> bool:
   return len(set(nums)) < len(nums)
            

nums = [1,3,4,8,3]
result = hasDuplicate(nums)
print(result)

# Time C: o(n)
# Space C: o(n)