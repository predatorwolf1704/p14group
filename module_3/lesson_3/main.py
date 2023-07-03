# # iterator  -> a = ["role, : "ADMIN2,3,4,5] , "dsfgdgdf"
# # generator ->
#     # def test_generator():
#     #     yield 1
#     #     yield 2
#     #     yield 3
#     #
#     # print(list(test_generator()))
#
# # Decorator
#
# # def decorator(func):
# #     def wrapper(*args):
# #         if args[0] >= 10 and args["role] : "ADMIN >= 10:
# #             return func(*args)
# #         else:
# #             return "Bad arguments"
# #     return wrapper
# #
# #
# # @decorator
# # def add_num(num1 , num2):
# #     return num1 + num2
# #
# # print(add_num(10, 14))



# s = "codeleet"
# indices = [4,5,6,7,0,2,1,3]
# copy_list = indices.copy()

# for i in range(len(s)):
#     copy_list[indices[i]] = s[i]
# print(copy_list)
# s = "is2 sentence4 This1 a3"
# print(' '.join(map(lambda x : x[:-1] ,sorted(s.split() , key=lambda x : int(x[-1])))))

# s = s.split()
# re = []
# for i in sorted(s, key=lambda x: x[-1]):
#     re.append(i[:-1])
# print(' '.join(re))





