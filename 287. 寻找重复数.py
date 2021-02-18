from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mapping = {}
        for right, v in enumerate(nums):
            if v in mapping.keys():
                return v
            mapping.update({v: right})

if __name__ == '__main__':
    solution = Solution()
    nums = [1,3,4,2,2]
    ans = solution.findDuplicate(nums)
    print(ans)