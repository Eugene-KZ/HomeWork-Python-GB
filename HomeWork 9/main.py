class TicTacToeBoard:
	def __init__(self):
		self.field = []
		for row in range(3):
			row_field = []
			for col in range(3):
				row_field.append('-')
			self.field.append(row_field)
		self.move = 'X'
		self.end_game = False
		self.win = ''
		

	def new_game(self):
		self.field = []
		for row in range(3):
			row_field = []
			for col in range(3):
				row_field.append('-')
			self.field.append(row_field)
		self.move = 'X'
		self.end_game = False
		self.win = ''



	def get_field(self):
		return self.field

	def check_field(self):
		if self.win == 'Ничья':
			return 'D'
		elif self.win == 'X':
			return 'X'
		elif self.win == 'O':
			return 'O'
		else:
			return None



	def make_move(self, row, col):
		if self.end_game:
			return 'Игра уже завершена'
		else:
			if self.field[row - 1][col - 1] != '-':
				return f'Клетка {row}, {col} уже занята.'
			else:
				if self.move == 'X':
					self.field[row - 1][col - 1] = 'X'
					self.move = 'O'
				else:
					self.field[row - 1][col - 1] = 'O'
					self.move = 'X'

				
				self.win_cord = ((0, 0, 1, 2), (1, 0, 1, 2), (2, 0, 1, 2))
				for i in self.win_cord:
					if (self.field[i[0]][i[1]] == self.field[i[0]][i[2]] == self.field[i[0]][i[3]]) and self.field[i[0]][i[1]] != '-':
						self.win = self.field[i[0]][i[1]]
						self.end_game = True
						return f'Победил игрок {self.field[i[0]][i[1]]}'
					elif (self.field[i[1]][i[0]] == self.field[i[2]][i[0]] == self.field[i[3]][i[0]]) and self.field[i[1]][i[0]] != '-':
						self.win = self.field[i[1]][i[0]]
						self.end_game = True
						return f'Победил игрок {self.field[i[1]][i[0]]}'
					elif (self.field[0][0] == self.field[1][1] == self.field[2][2]) or (self.field[0][2] == self.field[1][1] == self.field[2][0]) and self.field[1][1] != '-':
						self.win = self.field[1][1]
						self.end_game = True
						return f'Победил игрок {self.field[1][1]}'
					else:
						if ('-' not in self.field[0]) and ('-' not in self.field[1]) and ('-' not in self.field[2]):
							self.win = 'Ничья'
							self.end_game = True
							return 'Ничья'
						else:
							return 'Продолжаем игру'










a = TicTacToeBoard()
print(*a.get_field(), sep='\n')
print(a.make_move(1,1))
print(*a.get_field(), sep='\n')
print(a.make_move(1,1))
print(a.make_move(1,2))
print(*a.get_field(), sep='\n')
print(a.make_move(2,1))
print(a.make_move(2,2))
print(a.make_move(3,1))
print(a.make_move(2,2))
print(*a.get_field(), sep='\n')


