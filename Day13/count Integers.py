class Solution:
    def countEven(self, num: int) -> int:
        digits = []
        
        for i in range(1,num+1):
            d_sum = 0
            for j in str(i):
                d_sum += int(j)
            if d_sum %2 == 0:
                digits.append(i)
        return len(digits) 
