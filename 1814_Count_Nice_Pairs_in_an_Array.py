nums = [42,11,1,97]
res = 0
dict = {}
def rev(x: int):
    return int(str(x)[-1::-1])
for i in range(len(nums)):
    nums[i] = nums[i] - rev(nums[i])
    if nums[i] not in dict:
        dict[nums[i]] = 1
    else:
        dict[nums[i]] += 1
        res += dict[nums[i]] - 1

# for i in dict:
#     summing = 0
#     for i in range(dict[i]):
#         summing += i
#     res += summing
print(res%(109 + 7))
