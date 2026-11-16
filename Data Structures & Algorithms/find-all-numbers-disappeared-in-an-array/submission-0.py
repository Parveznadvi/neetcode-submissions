class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        output = [0] * (len(nums)+1)

        for i in range(len(nums)):
            output[nums[i]]=1
        
        j=0
        for i in range(1, len(output)):
            if output[i]==0:
                output[j]=i
                j+=1

        return output[0:j]