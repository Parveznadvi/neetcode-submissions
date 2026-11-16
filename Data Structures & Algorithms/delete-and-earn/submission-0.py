class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        freqLength = max(nums)+1
        freq = [0] * freqLength
        dp = [0] * freqLength

        for i in range(len(nums)):
            freq[nums[i]]+=nums[i]        

        dp[0]=freq[0]
        dp[1]=max(dp[0],freq[1])

        for i in range(2,len(freq)):
            dp[i]=max(dp[i-1], dp[i-2]+freq[i])

        return dp[freqLength-1]

