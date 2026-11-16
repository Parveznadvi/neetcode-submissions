class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sLen = len(s)
        tLen = len(t)

        isoDict = {}

        for i in range(sLen):
            if s[i] in isoDict:
                if isoDict[s[i]]!=t[i]:
                    return False 
            else:
                if t[i] in isoDict.values():
                    return False
                isoDict[s[i]]=t[i]
        
        return True
        