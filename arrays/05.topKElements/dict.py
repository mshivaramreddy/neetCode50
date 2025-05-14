from typing import List 
def topKFrequent(nums: List[int], k: int) -> List[int]:

    res = {}
    for num in nums:
        res[num] = 1+ res.get(num, 0)
        
    arr = []
    for num, c in res.items():
        arr.append([c, num])
    arr.sort()

    result = []
    while len(result) < k:
        result.append(arr.pop()[1])
    return result


nums = [1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3]
k = 2
result = topKFrequent(nums, k)
print(result)