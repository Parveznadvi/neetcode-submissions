class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        infinity=float('-inf')

        while low<=high:
            mid = low+(high-low)//2
            prev=mid-1
            nxt=mid+1
            prevNum = nums[prev] if prev>=0 else infinity
            nextNum = nums[nxt] if nxt<len(nums) else infinity
            
            if nums[mid]>prevNum and nums[mid]>nextNum:
                return mid

            if nextNum>prevNum:
                low=mid+1
            else:
                high=mid-1
        