class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        rows=len(matrix)
        cols=len(matrix[0])
        direction=0 # 1=MoveRight, 2=MoveDown, 3=MoveLeft, 4=MoveUp
        
        top=0
        left=0
        right=cols-1
        bottom=rows-1
        while top<=bottom and left<=right:
            for i in range(left,right+1):
                output.append(matrix[top][i])
            top+=1
            if left<=right:
                for i in range(top,bottom+1):
                    output.append(matrix[i][right])
                right-=1
            if top<=bottom:
                for i in range(right,left-1,-1):
                    output.append(matrix[bottom][i])
                bottom-=1
            if left<=right:
                for i in range(bottom,top-1,-1):
                    output.append(matrix[i][left])
                left+=1
        
        return output
        