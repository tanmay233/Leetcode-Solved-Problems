class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        res = []
        dict = {}
        for i in range(len(creators)):
            if creators[i] not in dict:
                dict[creators[i]] = [[ids[i]] , [views[i]],views[i]]
                continue
            dict[creators[i]][0].append(ids[i])
            dict[creators[i]][1].append(views[i])
            dict[creators[i]][2] += views[i]
        print(dict)
        maxpopularity = max([dict[_][2] for _ in dict])
        for i in dict:
            if dict[i][2] != maxpopularity:
                continue
            idies = dict[i][0]
            v = dict[i][1]
            m = max(v)
            r = [idies[_] for _ in range(0,len(v)) if v[_] == m]
            l = min([len(_) for _ in r])
            r = [_ for _ in r if len(_) == l]
            res.append([i,r[0]])
        return res
