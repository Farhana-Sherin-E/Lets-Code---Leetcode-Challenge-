class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        for k in range(0, len(arr), 2):
            arr[k], arr[k+1] = arr[k+1], arr[k]
        return arr
