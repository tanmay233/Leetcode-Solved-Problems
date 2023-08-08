class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target <= matrix[0][-1]:
            if target in matrix[0]:
                return (True)
            else:
                return (False)
            
        else:
            for i in range(len(matrix)):
                if matrix[i][-1] >= target:
                    if target in matrix[i]:
                        return (True)
                    else:
                        return (False)
                    break
