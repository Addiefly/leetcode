class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        mapping = {}
        max_len = 0
        sl = list(s)
        max_v = 0
        for right in range(len(sl)):
            if sl[right] not in mapping.keys():
                mapping.update({sl[right]: 1})
            else:
                mapping.update({sl[right]: mapping[sl[right]] + 1})
            max_v = max(mapping.values())
            while right -left + 1 - max_v > k:
                mapping[sl[left]] = mapping[sl[left]] - 1
                left = left + 1
            max_len = max(max_len, right - left + 1)
        print(mapping)
        return max_len

if __name__ == '__main__':
    so = Solution()
    s = "AABABBA"
    k = 1
    ans = so.characterReplacement(s, k)
    print(ans)