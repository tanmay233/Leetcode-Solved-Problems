import sys

# req_skills = ["java","nodejs","reactjs"]
# people = [["java"],["nodejs"],["nodejs","reactjs"]]
req_skills = ["algorithms","math","java","reactjs","csharp","aws"]
people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]

for i in range(len(people)-1):
    for j in range(i+1,len(people)):
        if len(people[i]) > len(people[j]):
            people[i] , people[j] = people[j] , people[i]

# people = [['nodejs', 'reactjs'], ['nodejs'], ['java']]


print(len(people))
x = len(str(bin(len(people)+(2**len(people)))[2:]))
print(x)
maxb = 2 ** x
arr = [0] * x
z = len(arr)
possibilities = []
for i in range(1,maxb):
    y = str(bin(i))[2:][-1::-1]
    # print(y)
    for j in range(len(y)):
        if y[j] == '1':
            arr[z-1-j] = 1
    possibilities.append(arr)
    arr = [0] * x
print(possibilities)
print(people)
res = [0] * x
sumz = sys.maxsize
for i in possibilities :
    dummy = []
    for j in range(len(i)):
        if i[j] == 1:
            dummy.extend([_ for _ in people[j]]) 
    temp = list(set(dummy))
    flag = 0
    if(all(x in temp for x in req_skills)):
        flag = 1
        if flag == 1:
            if sum(i) < sumz:
                res = i
                sumz = sum(i)
            print(res)

