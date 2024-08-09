my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
# цикл
while index < len(my_list):
    number = my_list[index]
    # приверка на отрицательные
    if number < 0:
        break
    # нули
    if number == 0:
        index += 1
        continue
    print(number)
    index += 1