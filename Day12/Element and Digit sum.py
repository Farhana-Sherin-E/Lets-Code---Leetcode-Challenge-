class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        E_sum, D_sum = 0, 0
        for i in nums:
            E_sum += i
            for j in str(i):
                D_sum += int(j)
        return abs(E_sum - D_sum) 
