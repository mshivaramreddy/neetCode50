def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

s = "racecar"
t = "carrace"
result = isAnagram(s,t)
print(result)

# Time C: o(nlogn + mlogm)
# Space C: o(n+m)