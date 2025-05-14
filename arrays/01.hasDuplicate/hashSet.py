from typing import List

def hasDuplicate(nums: List[int]) -> bool:
    checkSet = set()
    for num in nums:
        if num in checkSet:
            return True
        checkSet.add(num)
    
            

nums = [1,3,4,8,3]
result = hasDuplicate(nums)
print(result)

# Time C: o(n)
# Space C: o(n)