import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        ans = self.format_string(s)
        l = list(ans)
        for i in range(len(l)//2):
            if i == 0:
                if l[0] != l[-1]:
                    return False
            else:
                if l[i] != l[-i -1]:
                    return False
        return True

    def format_string(self, s):
        a = ""
        for i in list(s):
            if re.findall(r'\w', i) and i != '_':
                a = a + i
        b = a.lower()
        return b

if __name__ == '__main__':
    solution = Solution()
    s = "race a car"
    ans = solution.isPalindrome(s)
    print(ans)