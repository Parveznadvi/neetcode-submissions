class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        row = -1

        rowLow=0
        rowHigh=m-1
        while rowLow<=rowHigh:
            rowMid = rowLow + (rowHigh-rowLow)//2
            if target>=matrix[rowMid][0] and target<=matrix[rowMid][n-1]:
                row=rowMid
                break
            elif target<matrix[rowMid][0]:
                rowHigh = rowMid-1
            elif target>matrix[rowMid][n-1]:
                rowLow = rowMid+1
               
        if row!=-1:
            low = 0
            high = n-1
            while low<=high:
                mid = low + (high-low)//2
                if target == matrix[row][mid]:
                    return True
                elif target < matrix[row][mid]:
                    high = mid-1
                elif target > matrix[row][mid]:
                    low = mid+1
        
        return False


        