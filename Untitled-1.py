n = 8
k = 30
row = 6
column = 4

res = [[row,column]]
def moves(i,j):
    a = [[1,2],[-1,2],[1,-2],[-1,-2],[2,1],[-2,1],[2,-1],[-2,-1]]
    valid_moves = []
    for k in a:
        if 0<=i+k[0]<n and 0<=j+k[1]<n:
            valid_moves.append([i+k[0],j+k[1]])
    return valid_moves
# print(moves(0,0))
for r in range(k):
    x = len(res)
    for z in res[:x]:
        y = moves(z[0],z[1])
        res.extend(y)
    res = res[x:]
print(len(res)/(8**k))