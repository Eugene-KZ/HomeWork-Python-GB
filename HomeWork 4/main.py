# Вычислить число c заданной точностью d

# Пример:

# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


# number = float(input())
# d = float(input())
# if d == 1:
# 	print(int(number))
# else:
# 	d = len(str(d).split('.')[1])
# 	print(round(number, d))


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input())
# total_list = []
# for i in range(2, n + 1):
# 	if n % i == 0:
# 		for j in range(2, i // 2 + 1):
# 			if i % j == 0:
# 				break
# 		else:
# 			total_list.append(i)
# print(total_list)




# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# some_list = [1, 5, 15, 15, 0, 1 , 14]
# total_list = []
# for i in some_list:
# 	if some_list.count(i) == 1:
# 		total_list.append(i)
# print(total_list)



# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0



# import random

# k = int(input('Введите натуральную степень: '))
# koef = []
# total_list = []

# for _ in range(k + 1):
# 	rd_num = random.randint(0, 100)
# 	koef.append(rd_num)
# print(koef)


# for i in range(len(koef)-1):
# 	if k == 1:
# 		total_list.append(f'{koef[i]}x')
# 	else:
# 		total_list.append(f'{koef[i]}x^{k}')
# 	k -= 1
# total_list.append(str(koef[-1]))
# print(total_list)

# total_str = ''
# for i in range(len(total_list)-1):
# 	total_str += total_list[i] + ' + '
# total_str += total_list[-1] + ' = 0'
# print(total_str)

# with open('fille.txt', 'w', encoding='utf-8') as fille:
# 	fille.write(total_str)








# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.




total = []
with open('DZ-fille_1.txt', 'r', encoding='utf-8') as fille:
	fille_1 = fille.readline()
with open('DZ-fille_2.txt', 'r', encoding='utf-8') as fille:
	fille_2 = fille.readline()
print(fille_1)
print(fille_2)

fille_1 = fille_1.split(' =')[0].split(' + ')
fille_2 = fille_2.split(' =')[0].split(' + ')

for i in range(len(fille_1)):
	fille_1[i] = fille_1[i].split('x^')
for i in range(len(fille_2)):
	fille_2[i] = fille_2[i].split('x^')

temp = ''
ignor = []
for i in fille_1:

	for k in fille_2:

		if (len(k) == 2 and len(i) == 2) and ((('x^' + k[1]) not in ignor) and (('x^' + i[1]) not in ignor)):

			if int(k[1]) > int(i[1]):
				temp = k[0] + 'x^' + k[1]
				total.append(temp)
				ignor.append('x^' + k[1])

			elif int(k[1]) < int(i[1]):
				temp = i[0] + 'x^' + i[1]
				total.append(temp)
				ignor.append('x^' + i[1])

			elif int(k[1]) == int(i[1]):
				temp = str(int(k[0]) + int(i[0])) + 'x^' + k[1]
				total.append(temp)
				ignor.append('x^' + k[1])


		elif len(k) == 1 and len(i) == 1:

			if ('x' in i[0]) and ('x' in k[0]):
				temp = str(int(k[0].replace('x', '')) + int(i[0].replace('x', ''))) + 'x'
				total.append(temp)
				ignor.append('x^1')

			elif ((('x' in i[0]) and ('x' not in k[0])) or (('x' not in i[0]) and ('x' in k[0]))) and ('x^1' not in ignor):

				if ('x' in i[0]):
					temp = i[0]
					total.append(temp)
					ignor.append('x^1')
				elif ('x' in k[0]):
					temp = k[0]
					total.append(temp)
					ignor.append('x^1')

			elif ('x' not in i[0]) and ('x' not in k[0]):
				temp = str(int(k[0]) + int(i[0]))
				total.append(temp)
			
	
total_str = ''
for i in range(len(total) - 1):
	total_str += total[i] + ' + '
total_str += total[-1] + ' = 0'
with open('DZ-fille_3.txt', 'w', encoding='utf-8') as fille:
	fille.write(total_str)

print(total)
print(total_str)













