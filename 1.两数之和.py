"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。



示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution1(object):
    def twoSum(self, nums, target):
        """
        暴力解法
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


class Solution2(object):
    def twoSum(self, nums, target):
        """
        直接用target减去num，看看另一个数是否在数组里，用到nums.index(num)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            first_num = nums[i]
            target_num = target - first_num
            if target_num in nums:
                if i == nums.index(target_num):
                    continue
                else:
                    return [i, nums.index(target_num)]

if __name__ == "__main__":
    nums = [2, 5, 5, 11]
    target = 10

    # nums = [2, 7, 11, 15]
    # target = 9

    # nums = [3, 2, 4]
    # target = 6

    a = Solution2()
    print(a.twoSum(nums, target))

