class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            j = t.find(i)
            if j == -1:
                return False
            else:
                t = t[j+1:]
        return True