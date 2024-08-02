""" Дан список повторяющихся элементов.
Вернуть список с дублирующимися элементами.
В результирующем списке не должно быть дубликатов.
"""
my_list = [2,4,5,7,9,0,5,7,5,3,2,1]

dupl_list = []
for item in my_list:
    if my_list.count(item) > 1:
        dupl_list.append(item)

without_dupl_num = set(dupl_list)
print(without_dupl_num)
