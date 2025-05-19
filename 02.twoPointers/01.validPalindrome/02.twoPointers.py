def alphaNumericCheck(c):
    return (ord('A') <= ord(c) <= ord('Z') or
     ord('0') <= ord(c)<= ord('9') or
     ord('a') <= ord(c) <= ord('z'))

def validPalindrome(string: str) -> bool: 
    l, r = 0, len(string)-1
    while l<r:
        print(string[l], string[r])
        while l<r and not alphaNumericCheck(string[l]):
            print(string[l], string[r])
            l += 1
        while r>l and not alphaNumericCheck(string[r]):
            print(string[l], string[r])
            r -= 1
        if string[l].lower() != string[r].lower():
            return False
        l, r = l+1, r-1
    return True

string = "Was it a car or a cat I saw?"
result = validPalindrome(string)
print(result)




# time com: 
# space com: 