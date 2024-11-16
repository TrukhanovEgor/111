import numpy as np

# Создаем одномерный массив
array_1d = np.array([1, 2, 3, 4, 5])
print("Одномерный массив:", array_1d)

# Выполняем арифметические операции
array_squared = array_1d ** 2
print("Квадраты элементов:", array_squared)

# Находим среднее значение
mean_value = np.mean(array_1d)
print("Среднее значение:", mean_value)

# Создаем двумерный массив
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Двумерный массив:\n", array_2d)

# Транспонируем массив
transposed_array = np.transpose(array_2d)
print("Транспонированный массив:\n", transposed_array)

# Находим сумму по столбцам
column_sum = np.sum(array_2d, axis=0)
print("Сумма по столбцам:", column_sum)
