# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12



# some_list = [2, 9, 5, 10, 15, 3]
# summ = 0
# for i in range(1, len(some_list), 2):
# 	summ += some_list[i]
# print(summ)







# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


# some_list = [2, 9, 5, 5, 10, 15, 3]
# total_list = []
# for i in range((len(some_list) - 1) // 2 + 1):
# 	total_list.append(some_list[i] * some_list[len(some_list) - i -1])
# print(total_list)






# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19




# count = int(input("Введите колличество элементов: "))
# some_list = []
# for i in range(count):
# 	number = input()
# 	some_list.append(number)
# max = 0
# min = 1
# for i in some_list:
# 	if '.' in str(i):
# 		dr = str(i).split('.')[1]
# 		if float('0.' + dr) > max:
# 			max = float('0.' + dr)
# 		elif float('0.' + dr) < min:
# 			min = float('0.' + dr)
# print(max - min)




# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


# number = int(input('Введите число: '))
# binary = ''
# while number != 0:
# 	binary = str(number % 2) + binary
# 	number //=2
# print(binary)




# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# k = int(input('Введите k: '))
# some_list = [0] * (k * 2 + 1)
# some_list[k + 1] = 1
# for i in range(k + 2, len(some_list)):
# 	some_list[i] = some_list[i - 1] + some_list[i - 2]
# for i in range(k, - 1, -1):
# 	some_list[i] = some_list[i + 2] - some_list[ i + 1]
# print(some_list)