class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        currentplace = [0, 0]
        m = len(obstacleGrid[0]) - 1
        n = len(obstacleGrid) - 1

        

        def issafe(position):
            if position[0] <= n and position[1] <= m and obstacleGrid[position[0]][position[1]] == 0:
                return True
            return False

        def solution(currentplace, res):
            if obstacleGrid[0][0] == 1 or obstacleGrid[n][m] == 1:
                return 0
            if currentplace == [n, m]:
                if obstacleGrid[n][m] == 1:
                    return res
                res += 1
                return res
            
            right = [currentplace[0], currentplace[1] + 1]
            down = [currentplace[0] + 1, currentplace[1]]
            
            new_res = res
            
            if issafe(right):
                new_res = solution(right, new_res)
            if issafe(down):
                new_res = solution(down, new_res)
            
            return new_res

        final_res = solution([0, 0], 0)
        return final_res
