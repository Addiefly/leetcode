from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        largest = float('-inf')
        for i, num in enumerate(nums):
            sum = sum + num
            if i >= k:
                sum = sum - nums[i - k]
