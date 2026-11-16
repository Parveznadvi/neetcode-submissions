class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffDict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in diffDict:
                first = diffDict[difference]
                second = i
                return [first, second]
            diffDict[nums[i]] = i