class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)
        if sLen != tLen:
            return False
        sSorted = sorted(s)
        tSorted = sorted(t)
        for i in range(sLen):
            if sSorted[i] != tSorted[i]:
                return False
        return True