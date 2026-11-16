class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1

        if nums[low]<nums[high]:
            return nums[low]

        while low<=high:
            mid=low+(high-low)//2

            if nums[low]<nums[high]:
                return nums[low]

            if (mid==0 or nums[mid]<nums[mid-1]) and (mid==len(nums)-1 or nums[mid]<nums[mid+1]):
                return nums[mid]
            elif nums[mid]>=nums[low]:
                #left is sorted, go right
                low=mid+1
            elif nums[mid]<=nums[high]:
                #right is sorted, go left
                high=mid-1

        return low