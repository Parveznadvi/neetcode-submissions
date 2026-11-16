class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[0]*len(nums)

        output[0]=1
        for i in range(1,len(nums)):
            output[i]=output[i-1]*nums[i-1]

        sufProd=1
        for j in range(len(nums),1,-1):
            output[j-2]=sufProd*nums[j-1]*output[j-2]
            sufProd=sufProd*nums[j-1]

        return output