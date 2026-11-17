class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        mid=0
        high=len(nums)-1

        while mid<=high:
            if nums[mid]==0:
                # swap(low, mid)
                temp=nums[low]
                nums[low]=nums[mid]
                nums[mid]=temp
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            elif nums[mid]==2:
                #swap(mid, high)
                temp=nums[mid]
                nums[mid]=nums[high]
                nums[high]=temp
                high-=1
        
        return nums