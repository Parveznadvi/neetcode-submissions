class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)
        if sLen != tLen:
            return False
        sDict = {}
        for sChar in s:
            if sChar in sDict:
                sDict[sChar]=sDict[sChar]+1
            else:
                sDict[sChar]=1
        for tChar in t:
            if tChar in sDict:
                sDict[tChar]=sDict[tChar]-1
            else:
                return False
        for count in sDict.values():
            if count !=0:
                return False
        return True
