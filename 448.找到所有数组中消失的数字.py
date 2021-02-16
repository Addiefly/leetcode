from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        numset = set(nums)
        res = []
        num = 1
        for i in range(len(nums)):
            res.append(num)
            num = num + 1
        resset = set(res)
        ans = list(resset - numset)
        return ans


if __name__ == '__main__':
    nums = [2,2]
    solution = Solution()
    ans = solution.findDisappearedNumbers(nums)
    print(ans)
