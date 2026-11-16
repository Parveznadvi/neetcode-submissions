class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0

        count=0
        maxLen=0
        countDict={}
        countDict[0]=-1

        for i in range(len(nums)):
            if nums[i]==0:
                count-=1
            else:
                count+=1
            if count in countDict:
                maxLen=max(maxLen, (i-countDict[count]))
            else:
                countDict[count]=i
        
        return maxLen
