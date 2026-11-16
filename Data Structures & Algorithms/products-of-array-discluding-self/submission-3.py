class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProd=1
        sufProd=1
        prefix=[0]*len(nums)
        suffix=[0]*len(nums)
        output=[0]*len(nums)

        # zeroCount=0
        # zeroExists=False
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         zeroExists=True
        #         zeroCount+=1
        # if zeroCount>1:
        #     return output

        prefix[0]=1
        suffix[-1]=1
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]

        for j in range(len(nums),1,-1):
            suffix[j-2]=suffix[j-1]*nums[j-1]

        for k in range(len(nums)):
            output[k]=prefix[k]*suffix[k]

        return output

        