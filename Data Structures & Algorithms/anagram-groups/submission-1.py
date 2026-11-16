class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsLen = len(strs)
        if strsLen == 0:
            return [strs]
        
        sortedDict = {}
        groupedStrs = []
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord not in sortedDict:
                sortedDict[sortedWord]=[word]
            else:
                sortedDict[sortedWord].append(word)
        
        for key in sortedDict.keys():
            groupedStrs.append(sortedDict[key])
        
        return groupedStrs

        

            
