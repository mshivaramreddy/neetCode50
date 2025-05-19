from typing import List 
def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0]*n
    for i in range(n):
        sol = 1
        for j in range(n):
            if i == j:
                continue
            sol *= nums[j]
        
        res[i] = sol
    return res

nums = [1,2,4,6]
result = productExceptSelf(nums)
print(result)