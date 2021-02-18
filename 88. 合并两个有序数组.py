from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for k1, n1 in enumerate(nums1):
            if k1 >= m:
                nums1[k1] = nums2[-1]
                nums2.pop()
        nums1.sort()
        print(nums1)


if __name__ == '__main__':
    so = Solution()
    nums1 = [-1,0,0,3,3,3,0,0,0]
    m = 6
    nums2 = [1,2,2]
    n = 3
    so.merge(nums1, m, nums2, n)