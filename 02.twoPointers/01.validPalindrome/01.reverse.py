def validPalindrome(string: str) -> bool: 
    res = ''
    for char in string:
        if char.isalnum():
            res += char.lower()
    return res == res[::-1]

string = "Was it a car or a cat I sawh "
result = validPalindrome(string)
print(result)


# time com: o(n)
# space com: o(n)