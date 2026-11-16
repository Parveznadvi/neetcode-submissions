class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        maxArea=0
        left=0
        right=n-1

        while left<right:
            minHeight=min(heights[left], heights[right])
            width=right-left
            area=minHeight*width
            maxArea=max(maxArea,area)
            if minHeight==heights[left]:
                left+=1
            else:
                right-=1

        return maxArea