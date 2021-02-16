from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        length = len(arr)
        if len(set(arr)) == 1:
            return 1
        elif length <= 2:
            return length

        maxLength = 2
        LengthState = 2
        for i in range(length - 3, -1, -1):
            if arr[i] > arr[i + 1] < arr[i + 2] or arr[i] < arr[i + 1] > arr[i + 2]:
                LengthState += 1
                maxLength = max(maxLength, LengthState)
            else:
                LengthState = 2
        return maxLength


if __name__ == '__main__':
    solution = Solution()
    arr = [9,9]
    ans = solution.maxTurbulenceSize(arr)
    print(ans)