import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

old_list.append([4, 4, 4])
new_list.append([5, 5, 5])

old_list[0][0] = 'A'
new_list[0][0] = 'B'

print("Old list:", old_list)
print("New list:", new_list)
