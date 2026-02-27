class Solution(object):
    def averageValue(self, nums):
        sum, count = 0,0
        for i in nums:
            if (i % 2 == 0) and (i % 3 == 0):
                sum += i
                count += 1
        if count == 0:
            return 0
        return (sum // count)
