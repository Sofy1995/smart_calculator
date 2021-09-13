from collections.abc import Hashable


#object_list = [1, 397, 27468, -95, 1309, 397, -539874, -240767, -95, 397]
#object_list = [1, 27468, 1309, 397, -539874, -240767, -95]
#print(object_list)
# duplicates = 0
elements = 0

# for some_l in object_list:
#     if isinstance(some_l, Hashable) is False:
#         object_list.remove(some_l)
# #print(object_set)
# object_set = set(object_list)
# for some_s in object_set:
#     if isinstance(some_s, Hashable):
#         for some_l in object_list:
#             if isinstance(some_l, Hashable):
#                 if some_s.__eq__(some_l):
#                     duplicates += 1
#         if duplicates > 1:
#             elements += duplicates
#         duplicates = 0
# print(elements)


freq_dict = {}

for some_l in object_list:
    # set the default value to 0
    if isinstance(some_l, Hashable):
        freq_dict.setdefault(some_l, 0)
        # increment the value by 1
        freq_dict[some_l] += 1

for value in freq_dict.values():
    if value > 1:
        elements += value

print(elements)
