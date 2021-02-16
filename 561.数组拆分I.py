from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for idx, num in enumerate(nums):
            if idx % 2 == 0:
                ans += num
        return ans


if __name__ == '__main__':
    nums = [6, 2, 6, 5, 1, 2]
    solution = Solution()
    ans = solution.arrayPairSum(nums)
    print(ans)
