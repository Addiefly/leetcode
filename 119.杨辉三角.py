from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lastRow = [1]
        for i in range(rowIndex):
            nextRow = self.getNextRow(lastRow)
            lastRow = nextRow
            print("AAAAAAA", nextRow, lastRow, "BBBBBBBBBBB")
        return lastRow

    def getNextRow(self, lastRow):
        nextRow = [1]
        if len(lastRow) == 1:
            # nextRow = [1, 1]
            return [1, 1]
        else:
            for i in range(len(lastRow) - 1):
                nextRow.append(lastRow[i] + lastRow[i + 1])
            print("getNextRow", nextRow)
        nextRow.append(1)
        return nextRow


if __name__ == '__main__':
    solution = Solution()
    ans = solution.getRow(4)
    print(ans)