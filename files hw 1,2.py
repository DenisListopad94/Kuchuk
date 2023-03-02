# # file hw
# 1
# f = open('hw_file.txt', 'r', encoding='UTF-8')
# some_str = f.read()
# f.close()
# some_str = some_str.split()
# for i in range(0, len(some_str)):
#     if some_str[i][-1] == '!':
#         print(some_str[i])
# print(some_str)

# 2
# file = open('input.txt', 'r', encoding='UTF-8')
# some_str = file.read()
# file.close()
# lst = some_str.replace('\n',' ').split()
# lst = list(map(int,lst))
# def proizv(lst):
#     count = 1
#     for i in lst:
#         count *=i
#     return count
# print(str(proizv([45,2,1,23,54,17,45,62,21,84])))
#
# f = open("output.txt", 'w', encoding= 'UTF-8')
# f.write(str(proizv([45,2,1,23,54,17,45,62,21,84])))
# f.close()