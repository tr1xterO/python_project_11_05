my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
if my_new_list[0] > my_new_list[-1]:
    my_new_list.pop(0)
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')