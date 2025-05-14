# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]


from collections import defaultdict
from typing import List
def groupAnagram(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)    
    for s in strs:
        sortedS = ''.join(sorted(s))
        res[sortedS].append(s)
    return list(res.values())
    

strs = ["act","pots","tops","cat","stop","hat"]
result = groupAnagram(strs)