from typing import List
def twoSum(number: List[int], target: int) -> List[int]:
    l, r = 0, len(number)-1
    while l<r:
        sum = number[l] + number[r]
        if sum > target:
            r -= 1
        elif sum < target:
            l += 1
        else:
            return [l+1, r+1]
    return []


number, target = [1,2,3,4], 3
result = twoSum(number, target)
print(result)


# TC: o(n)
# SP: o(1)