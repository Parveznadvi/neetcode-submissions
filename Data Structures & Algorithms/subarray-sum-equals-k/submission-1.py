class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        countDict={}
        countDict[0]=1
        count=0
        runningCount=0

        for i in range(len(nums)):
            runningCount+=nums[i]
            if (runningCount-k) in countDict:
                count=count+countDict[runningCount-k]
                countDict[runningCount]=countDict.get(runningCount, 0) + 1
            else:
                countDict[runningCount]=countDict.get(runningCount, 0) + 1
        
        return count