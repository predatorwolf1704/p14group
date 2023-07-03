# https://leetcode.com/problems/running-sum-of-1d-array/
# nums = [1, 2, 3, 4]
# c = 0
# re = []
# for i in nums:
#     c += i
#     re.append(c)
# print(re)

# print([sum(nums[:i])for i in range(1, len(nums) +1)])
# print(list(map(lambda x : sum(nums[:x]) , range(1, len(nums) +1))))


# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

# sentences = [
#     "alice and bob love leetcode",
#     "i think so too",
#     "this is great thanks very much"]
#
# # max_ = float("-inf")
# #
# # for i in sentences:
# #     max_ = max(max_ , len(i.split()))
# #
# # print(max_)
#
# print(max([len(i.split()) for i in sentences]))
# print(max(map(lambda x : len(x.split()) , sentences)))
# print(len(sorted(sentences , key = lambda x : len(x.split()))[-1].split()))

# https://leetcode.com/problems/create-target-array-in-the-given-order/
# nums = [0,1,2,3,4]
# index = [0,1,2,2,1]
#
# r = []
# for i in range(len(nums)):
#     r.insert(index[i] , nums[i])
# print(r)

# nums = [1,2,3,1,1,3]
# print(sum(map(lambda x: nums[x[0] + 1:].count(x[1]), enumerate(nums))))
# from string import ascii_lowercase
#
# key = "the quick brown fox jumps over the lazy dog"
# message = "vkbs bs t suepuv"
# alfa = "abcdefghijklmnopqrstuvwxyz"
#
# key = key.replace(" ","")
# orginal_key = ""
# for i in key:
#     if not i in orginal_key:
#         orginal_key += i
#
# res = ""
# for i in message:
#     if i == " ":
#         res += i
#         continue
#     res += alfa[orginal_key.index(i)]
# print(res)


# from string import ascii_uppercase as au
#
# s = "K1:L2"
# s = s.split(":")
# min_num = int(s[0][-1])
# max_num = int(s[1][-1])
# re = []
# for i in au[au.index(s[0][0]) : au.index(s[1][0]) + 1]:
#     for j in range(min_num, max_num+ 1):
#         re.append(f"{i}{j}")
# print(re)

# https://leetcode.com/problems/delete-greatest-value-in-each-row/
#
# grid = [
#     [1, 2, 4 , 8],
#     [1, 3, 3 , 9]
# ]
# for i in grid:
#     i.sort()
# print(sum([max(i) for i in zip(*grid)]))

# print(*zip([1], [3, 4]))
#
# grid = [
#     [1, 2, 4 , 8],
#     [1, 3, 3 , 9]
# ]

# 1 1
# 3 2
# 3 4
# 9 8

# names = ["Mary","John","Emma"]
# heights = [180,165,170]
#
# l = list(zip(names, heights))
# sorted_l = sorted(l , key=lambda x : x[1] , reverse=True)
# re = []
# for i in sorted_l:
#     re.append(i[0])
# print(re)


# print(list(map(lambda x : x[0],sorted(zip(names , heights) , key=lambda x: x[1], reverse=True))))


# seats = [2,2,6,6]
# students = [1,3,2,6]
#
# seats.sort()
# students.sort()
# print(sum([abs(i[0] - i[1]) for i in zip(seats , students)]))


arr = [3,0,1,1,9,7]

a = 7
b = 2
c = 3
re = 0
for i in range(len(arr)):
    for j in range(i + 1 ,len(arr)):
        for k in range(j + 1 , len(arr)):
            if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                re += 1
print(re)










