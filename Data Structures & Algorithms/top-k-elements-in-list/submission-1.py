class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1
        
        numsLen = len(nums)
        bucket = [[] for _ in range(numsLen+1)]

        for key, value in freqMap.items():
            bucket[value].append(key)

        res=[]
        for i in range(numsLen, 0, -1):
            for num in bucket[i]:
               res.append(num)
               if len(res)==k:
                return res 
        