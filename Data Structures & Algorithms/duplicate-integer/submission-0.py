class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = {}
        if len(nums) == 0:
            return False
        for i in nums:
            if i in unique:
                return True
            else:
                unique[i]=i
        return False
            
