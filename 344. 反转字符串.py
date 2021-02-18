from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        print(s)


if __name__ == '__main__':
    so = Solution()
    s = ["h", "e", "l", "l", "o"]
    so.reverseString(s)