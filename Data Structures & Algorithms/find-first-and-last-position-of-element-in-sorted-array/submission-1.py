class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1

        startIdx=-1
        endIdx=-1

        if len(nums)==0 or target<nums[0] or target>nums[high]:
            return [startIdx, endIdx]

        # Find Start Index
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                if mid==0 or nums[mid]>nums[mid-1]:
                    startIdx=mid
                    break
                else:
                    high=mid-1
            elif nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
        
        low=startIdx
        high=len(nums)-1
        
        # Find End Index
        while low<=high:
            mid=low+(high-low)//2
            if nums[mid]==target:
                if mid==len(nums)-1 or nums[mid]<nums[mid+1]:
                    endIdx=mid
                    break
                else:
                    low=mid+1
            elif nums[mid]<target:
                low=mid+1
            elif nums[mid]>target:
                high=mid-1

        return [startIdx, endIdx]