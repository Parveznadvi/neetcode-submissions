class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s)==1:
            return 1
        
        sLen = len(s)
        charCount={}
        maxLen=0
        needToAddOne = False

        for c in s:
            if c in charCount:
                charCount[c]+=1
            else:
                charCount[c]=1
        
        countList = list(charCount.values())

        for count in countList:
            if count%2==0:
                maxLen+=count
            else:
                maxLen=maxLen+(count-1)
                needToAddOne = True
        
        if needToAddOne:
             return maxLen+1 
        return maxLen


        

        