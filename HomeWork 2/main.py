# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# num = input("Введите число: ")
# len_num = len(num)
# sum = 0
# for i in range(len_num):
# 	if num[i] == "," or num[i] == ".":
# 		i+=1
# 	else:
# 		sum += int(num[i])
# print(sum) 





# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Пример:

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input("Введите N: "))
# total = []
# multi = 1
# for i in range(1, n+1):
# 	multi*= i
# 	total.append(multi)
# print(total)





# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# Пример:

# Для N = 4, тогда {1:2, 2:2,25, 3:2,27, 4:2,44}

# Сумма: 9,06



# n = int(input("Введите N: "))
# sum = 0
# for i in range(1, n+1):
# 	a = (1 + (1/i))**i
# 	sum += a
# print(round(sum, 2))




# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = [-8, 3, 7, -2, -6, 4]
total = 1
with open('index.txt', 'r') as file_1:
	for line in file_1:
		i = int(line)
		total *= n[i]
print(total)








# Реализуйте алгоритм перемешивания списка.


# import random

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i in range(len(list)):
# 	temp = 0
# 	r = random.randint(0,len(list)-1)
# 	temp = list[i]
# 	list[i] = list[r]
# 	list[r] = temp
# print(list)



# ДОП. задача на алгоритмы с реальных собеседований
# Даны два массива:
# [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
# Надо вернуть их пересечение
# [1, 2, 2, 3]
# (порядок не важен)

# array_1 = [1, 2, 3, 2, 0]
# array_2 = [5, 1, 2, 7, 3, 2]
# total_array = []
# index_delet = []

# for i in range(len(array_1)):
# 	for j in range(len(array_2)):
# 		if array_1[i] == array_2[j] and not (j in index_delet):
# 			total_array.append(array_1[i])
# 			index_delet.append(j)
# 			break
# print(total_array)

