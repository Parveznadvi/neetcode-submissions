class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        target=0

        for i in range(len(nums)-2):
            if i>0 and (nums[i]==nums[i-1]):
                continue
            left=i+1
            right=len(nums)-1

            while left<right:
                if nums[i]+nums[left]+nums[right]==target:
                    result.append([nums[i],nums[left],nums[right]])
                    moveHowMany=1
                    while left+moveHowMany<right and nums[left+moveHowMany]==nums[left]:
                        moveHowMany+=1
                    left+=moveHowMany
                    moveHowMany=1
                    while right-moveHowMany>left and nums[right-moveHowMany]==nums[right]:
                        moveHowMany+=1
                    right-=moveHowMany
                elif nums[i]+nums[left]+nums[right]<target:
                    left+=1
                elif nums[i]+nums[left]+nums[right]>target:
                    right-=1
        
        return result



