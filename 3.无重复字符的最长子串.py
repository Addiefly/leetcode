class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        mapping = {}
        for right, v in enumerate(s):
            if v in mapping:
                left = max(mapping.get(v) + 1, left)
            max_len = max(max_len, right - left + 1)
            mapping[v] = right
        return max_len


if __name__ == '__main__':
    solution = Solution()
    s = "abcabcbb"
    ans = solution.lengthOfLongestSubstring(s)
    print(ans)