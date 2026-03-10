class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        rev = ""
        for i in s:
            rev = i + rev
        return rev == s
