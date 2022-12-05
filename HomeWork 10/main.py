# class MinStat:
# 	def __init__(self):
# 		self.number = []
	
# 	def add_number(self, num):
# 		self.number.append(num)


# 	def result(self):

# 		if len(self.number) != 0:
# 			minn = self.number[0]
# 			for i in self.number:
# 				if i < minn:
# 					minn = i
# 			return minn
# 		else:
# 			return None

# class MaxStat:
# 	def __init__(self):
# 		self.number = []
	
# 	def add_number(self, num):
# 		self.number.append(num)


# 	def result(self):

# 		if len(self.number) != 0:
# 			maxx = self.number[0]
# 			for i in self.number:
# 				if i > maxx:
# 					maxx = i
# 			return maxx
# 		else:
# 			return None


# class AverageStat:
# 	def __init__(self):
# 		self.number = []
	
# 	def add_number(self, num):
# 		self.number.append(num)


# 	def result(self):

# 		if len(self.number) != 0:
# 			ave = 0
# 			for i in self.number:
# 				ave += i
# 			ave /= len(self.number)
# 			return ave
# 		else:
# 			return None


# values = [1, 0, 0]

# mins = MinStat()
# maxs = MaxStat()
# average = AverageStat()

# for v in values:
# 	mins.add_number(v)
# 	maxs.add_number(v)
# 	average.add_number(v)

# print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))



# table.get_value(row, col) — прочитать значение из ячейки в строке row, столбце col. Если ячейка с индексами row и col не лежит внутри таблицы, нужно вернуть None.

# table.set_value(row, col, value) — записать число в ячейку строки row, столбца col. Гарантируется, что в тестах будет в запись только в ячейки внутри таблицы.

# table.n_rows() — вернуть число строк в таблице

# table.n_cols() — вернуть число столбцов в таблице

# table.delete_row(row) — удалить строку с номером row

# table.delete_col(col) — удалить колонку с номером col

# table.add_row(row) — добавить в таблицу новую строку с индексом row.
# Номера строк >= row, должны увеличиться на единицу. Новая строка состоит из нулей.

# table.add_col(col) — добавить в таблицу новую колонку с индексом col.
# Номера колонок >= col, должны увеличиться на единицу. Новая колонка состоит из нулей.

class Table:
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.table = []
		for r in range(self.row):
			row_field = []
			for c in range(self.col):
				row_field.append(0)
			self.table.append(row_field)

	def get_value(self, row, col):
		if (row > self.row - 1) or (col > self.col - 1) or (row < 0) or (col < 0):
			return None
		else:
			return self.table[row][col]


	def set_value(self, row, col, value):
		self.table[row][col] = value

	def n_rows(self):
		return self.row

	def n_cols(self):
		return self.col

	def add_row(self, row):
		row_add = []
		for i in range(self.col):
			row_add.append(0)
		self.table.insert(row, row_add)
		self.row += 1

	def add_col(self, col):
		for i in range(self.row):
			self.table[i].insert(col, 0)
		self.col += 1



	def delet_row(self, row):
		self.table.pop(row)
		self.row -= 1

	def delet_col(self, col):
		for i in range(self.row):
			self.table[i].pop(col)
		self.col -= 1






# Пример 1

# tab = Table(3, 5)
# tab.set_value(0, 1, 10)
# tab.set_value(1, 2, 20)
# tab.set_value(2, 3, 30)

# for i in range(tab.n_rows()):
# 	for j in range(tab.n_cols()):
# 		print(tab.get_value(i, j), end=' ')
# 	print()
# print()

# tab.add_row(1)

# for i in range(tab.n_rows()):
# 	for j in range(tab.n_cols()):
# 		print(tab.get_value(i, j), end=' ')
# 	print()
# print()



# Пример 2

# tab = Table(2, 2)

# for i in range(tab.n_rows()):
# 	for j in range(tab.n_cols()):
# 		print(tab.get_value(i, j), end=' ')
# 	print()
# print()

# tab.set_value(0, 0, 10)
# tab.set_value(0, 1, 20)
# tab.set_value(1, 0, 30)
# tab.set_value(1, 1, 40)

# for i in range(tab.n_rows()):
# 	for j in range(tab.n_cols()):
# 		print(tab.get_value(i, j), end=' ')
# 	print()
# print()

# for i in range(-1, tab.n_rows() + 1):
# 	for j in range(-1, tab.n_cols() + 1):
# 		print(tab.get_value(i, j), end=' ')
# 	print()
# print()

# tab.add_row(0)
# tab.add_col(1)

# for i in range(-1, tab.n_rows() + 1):
# 	for j in range(-1, tab.n_cols() + 1):
# 		print(tab.get_value(i, j), end=' ')
# 	print()
# print()


# Пример 3

tab = Table(1, 1)

for i in range(tab.n_rows()):
	for j in range(tab.n_cols()):
		print(tab.get_value(i, j), end=' ')
	print()
print()

tab.set_value(0, 0, 1000)

for i in range(tab.n_rows()):
	for j in range(tab.n_cols()):
		print(tab.get_value(i, j), end=' ')
	print()
print()

for i in range(-1, tab.n_rows() + 1):
	for j in range(-1, tab.n_cols() + 1):
		print(tab.get_value(i, j), end=' ')
	print()
print()

tab.add_row(0)
tab.add_row(2)
tab.add_col(0)
tab.add_col(2)

tab.set_value(0, 0, 2000)
tab.set_value(0, 2, 3000)
tab.set_value(2, 0, 4000)
tab.set_value(2, 2, 5000)

for i in range(-1, tab.n_rows() + 1):
	for j in range(-1, tab.n_cols() + 1):
		print(tab.get_value(i, j), end=' ')
	print()
print()
