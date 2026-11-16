class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            if num not in freqMap:
                freqMap[num] = 1
            else:
                freqMap[num]+=1
        
        flipped = [[freq,num] for num, freq in freqMap.items()]

        flipped.sort(reverse=True)

        return [num for freq,num in flipped[:k]]

        

