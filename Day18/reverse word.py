class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        arr = []
        for i in s:
            arr.append(i[::-1])
        return " ".join(arr)
