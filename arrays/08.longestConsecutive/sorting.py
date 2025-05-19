from typing import List
def longConsecutive(nums: List[int]) -> int:
    a = sorted(nums)
    result = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if nums[i]+1 == nums[j]:
                result += 1 
    return result


# nums = [2,20,10,3,4,5]
nums = [0,3,2,5,4,6,1,1]
result = longConsecutive(nums)
print(result)