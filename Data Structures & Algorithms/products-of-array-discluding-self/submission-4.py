class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[0]*len(nums)
        suffix=[0]*len(nums)
        output=[0]*len(nums)

        prefix[0]=1
        suffix[-1]=1
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]

        for j in range(len(nums),1,-1):
            suffix[j-2]=suffix[j-1]*nums[j-1]

        for k in range(len(nums)):
            output[k]=prefix[k]*suffix[k]

        return output

        