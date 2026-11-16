class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        rows = len(coins)
        cols = amount 
        dpArray = [[0] * (cols+1) for _ in range(rows+1)]

        for row in range(rows+1):
            dpArray[row][0]=1

        for row in range(1, rows+1):
            for col in range(1,cols+1):
                if coins[row-1]>col:
                    dpArray[row][col]=dpArray[row-1][col]
                else:
                    dpArray[row][col]=dpArray[row-1][col]+dpArray[row][col-coins[row-1]]
        
        return dpArray[rows][cols]


        