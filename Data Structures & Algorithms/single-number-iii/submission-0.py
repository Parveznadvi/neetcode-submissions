class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        num=nums[0]  #1
        for i in range(1, len(nums)):
            num^=nums[i]
        
        numTcomp = (~num+1) & ((1<<8)-1) #2

        temp = num & numTcomp #3
        firstNum = 0 #4
        for i in range(len(nums)):
            if nums[i] & temp != 0:
                firstNum^=nums[i]   #5
            
        secondNum=firstNum ^ num

        return [firstNum, secondNum]
        

