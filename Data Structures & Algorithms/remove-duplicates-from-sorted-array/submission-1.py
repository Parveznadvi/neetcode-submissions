class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
     
        if len(nums)==1:
            return 1

        p1=0
        p2=1

        while p2<len(nums):
            #Same
            if nums[p1]==nums[p2]:
                while p2<len(nums) and nums[p2]==nums[p1]:
                    p2+=1
                if p2==len(nums):
                    return p1+1
                p1+=1
                nums[p1]=nums[p2]
                p2+=1
            
            #Not Same
            elif nums[p1]!=nums[p2]:
                if p2-p1!=1:
                    p1+=1
                    nums[p1]=nums[p2]
                    p2+=1
                else:
                    p1+=1
                    p2+=1

        return p1+1


        