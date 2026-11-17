class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroCounter=0
        oneCounter=0
        twoCounter=0

        for i in range(len(nums)):
            if nums[i]==0:
                zeroCounter+=1
            if nums[i]==1:
                oneCounter+=1
            if nums[i]==2:
                twoCounter+=1
        
        j=0
        while zeroCounter!=0:
            nums[j]=0
            j+=1
            zeroCounter-=1
        while oneCounter!=0:
            nums[j]=1
            j+=1
            oneCounter-=1
        while twoCounter!=0:
            nums[j]=2
            j+=1
            twoCounter-=1

        return nums
