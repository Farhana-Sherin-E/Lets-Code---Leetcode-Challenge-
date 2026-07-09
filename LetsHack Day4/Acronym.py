class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        x = ""
        for i in words:
            x += i[0]
        if s==x:
            return True
        else:
            return False
