class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):            
            if target <= matrix[i][n-1]:
                low = 0
                high = n-1
                while low<=high:
                    mid = low + (high-low)//2
                    if target == matrix[i][mid]:
                        return True
                    elif target < matrix[i][mid]:
                        high = mid-1
                    elif target > matrix[i][mid]:
                        low = mid+1
        return False