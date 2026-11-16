class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        if len(nums) == 0:
            return False
        for num in nums:
            if num in unique:
                return True
            unique.add(num)
        return False
            
        