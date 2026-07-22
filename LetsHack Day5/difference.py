class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count={}
        for i in s:
            if i  in count:
                count[i] +=1
            else:
                count[i] = 1

        for j in t:
            if j not in count:
                return j
            count[j] -= 1
        
            if count[j] < 0:
                return j
