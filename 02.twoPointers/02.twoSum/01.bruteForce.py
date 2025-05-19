from typing import List
def twoSum(number: List[int], target: int) -> List[int]:
    for i in range(len(number)):
        for j in range(1, len(number)):
            if number[i] + number[j] == target:
                return [i+1, j+1]
    return []


number, target = [1,2,3,4], 3
result = twoSum(number, target)
print(result)


# TC: o(n2)
# SP: o(1)