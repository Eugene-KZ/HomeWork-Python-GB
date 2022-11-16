# Дан список: ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками 
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

# Подумать, какое условие записать, чтобы выявить числа среди элементов списка? 
# Как модифицировать это условие для чисел со знаком?
# Примечание: если обособление чисел кавычками не будет получаться - можете вернуться к
#  его реализации позже. Главное: дополнить числа до двух разрядов нулём!

# input_array = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# for _ in range(len(input_array)):

# 	element = input_array.pop(0)

# 	if element.isdigit():
# 		input_array.append(f'"{int(element):02d}"')

# 	elif element[0] == "+" and element[1].isdigit():
# 		input_array.append(f'"+{int(element):02d}"')

# 	else:
# 		input_array.append(element)
# print(' '.join(input_array))






# Дан список, содержащий искажённые данные с должностями и именами сотрудников:
#  ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# Известно, что имя сотрудника всегда в конце строки. Сформировать и вывести на экран фразы вида:
#  'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов списка, как привести их
#   к корректному виду. Можно ли при этом не создавать новый список?



# input_array = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

# for i in range(len(input_array)):
# 	input_array[i] = input_array[i].split()
# 	temp = ''
# 	for j in range(len(input_array[i]) - 1):
# 			temp = temp +  input_array[i][j] + ' '
# 	temp = temp + input_array[i][-1].capitalize()
# 	name = input_array[i][-1].capitalize()
# 	input_array[i] = temp
		
# 	print(input_array)
# 	print(f"Привет, {name}!")



# Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]

# Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
#  Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек 
#  (должно быть 07 коп или 00 коп).
# Вывести цены, отсортированные по возрастанию, новый список не создавать 
# (доказать, что объект списка после сортировки остался тот же).
# Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?


input_array = [57.8, 46.51, 97, 22.14, 33.42, 39.33, 89.43, 29.66, 38.01, 14.00, 0.22, 1, 67, 23.99, 99.99, 73.01]

print(input_array , '\n')

input_array.sort()
print(input_array , '\n')

revers_array = sorted(input_array, reverse=True)
print(revers_array , '\n')

end_word: str = ", "

for i, num in enumerate(input_array):

	fix_price = str(f"{float(num):.2f}").split(".")

	if i == len(input_array) - 1:
		end_word = "\n"

	print(f"{fix_price[0]} руб {fix_price[1]} коп", end=end_word)