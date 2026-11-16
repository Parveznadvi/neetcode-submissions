class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        rows=len(coins)
        cols=amount
        minCoinsMatrix=[[0] * (cols+1) for _ in range(rows+1)]

        for col in range(1,cols+1):
            minCoinsMatrix[0][col]=99999

        for row in range(1,rows+1):
            for col in range(1,cols+1):
                if coins[row-1]>col: 
                    minCoinsMatrix[row][col]=minCoinsMatrix[row-1][col]
                else:
                    minCoinsMatrix[row][col]=min(minCoinsMatrix[row-1][col], 1 + minCoinsMatrix[row][col - coins[row-1]])
                    
        if (minCoinsMatrix[rows][cols] == 99999): return -1
        return minCoinsMatrix[rows][cols]


    # def helper(self, coins: List[int], amount: int, idx: int, minCoins: int) -> int:
    #     // Base case
    #     if(amount<0 || idx=len(coins)) return -1
    #     if(amount==0) return minCoins

    #     // Logic
    #     // Dont-take
    #     case1 = helper(coins, amount, idx+1, minCoins)
    #     // Take
    #     case2 = helper(coins, amount-coins[idx], idx, minCoins+1)

    #     if(case1==-1) return case2
    #     if(case2==-1) return case1

    #     return min(case1,case2)
        


