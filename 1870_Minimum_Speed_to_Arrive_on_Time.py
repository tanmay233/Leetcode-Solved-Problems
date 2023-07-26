class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def check(x):
            time = 0
            for i in range(len(dist)-1):
                time += math.ceil(dist[i]/x)
            time += dist[-1]/x
            if time <= hour:
                return True
            else:
                return False
            
        l = 0
        r = (10 ** 7) + 1
        found = 0
        res = 0
        while True:
            mid = int((l + r) / 2)
            c = check(mid)
            if c == True:
                found = 1
                res = mid
                r = mid
            else:
                l = mid
            if l == r or l+1 == r:
                break
        if res == 0:
            return -1
        return res
