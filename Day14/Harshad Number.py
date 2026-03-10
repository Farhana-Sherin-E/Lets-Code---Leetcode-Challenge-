class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        d_sum = 0
        for i in str(x):
            d_sum += int(i)
        if (x % d_sum == 0):
            return d_sum
        else:
            return -1
