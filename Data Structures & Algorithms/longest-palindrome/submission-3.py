class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s)==1:
            return 1

        charSet = set()
        maxPLen=0

        for char in s:
            if char in charSet:
                charSet.remove(char)
                maxPLen+=2
            else:
                charSet.add(char)
        
        if charSet:
            maxPLen+=1

        return maxPLen
        
        