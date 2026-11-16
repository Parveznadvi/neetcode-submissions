class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=1
        zeroExists=False
        zeroCount=0
        for i in range(len(nums)):
            if nums[i]!=0:
                prod*=nums[i]
            else:
                zeroExists=True
                zeroCount+=1

        output=[0]*len(nums)

        if zeroExists:
            if zeroCount>1:
                prod=0
            for i in range(len(nums)):
                if nums[i]==0:
                    output[i]=prod
        else:
            for i in range(len(nums)):
                output[i]=prod//nums[i]

        return output