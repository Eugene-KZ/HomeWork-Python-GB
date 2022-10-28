# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = input()
# text = text.split()
# new_tex = list(filter(lambda x: 'абв' not in x, text))
# print(new_tex)


# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
#  чтобы забрать все конфеты у своего конкурента?

# import random

# def input_candies(player):
# 	input_candi = int(input(f"{player}, введите количество конфет, которое возьмете от 1 до 28: "))
# 	while input_candi < 1 or input_candi > 28:
# 		input_candi = int(input("Введите корректное количество конфет: "))
# 	return input_candi

# def conclusion(player, candies, cand, count):
# 	print(f'Игрок {player}, взял {cand} конфет. Всего у игрока {count} конфет, на столе осталось {candies} конфет')


# candies = 200

# player_1 = input('Введите имя первого игрока: ')
# player_2 = input('Введите имя второго игрока: ')


# turn = random.randint(0, 1)
# if turn == 0:
# 	print(f'Первым ходит {player_1}')
# else:
# 	print(f'Первым ходит {player_2}')

# count_1 = 0
# count_2 = 0

# while candies > 28:
# 	if turn == 0:
# 		cand = input_candies(player_1)
# 		candies -= cand
# 		count_1 += cand
# 		conclusion(player_1, candies, cand, count_1)
# 		turn = 1

# 	else:
# 		cand = input_candies(player_2)
# 		candies -= cand
# 		count_2 += cand
# 		conclusion(player_2, candies, cand, count_2)
# 		turn = 0
# if turn == 0:
# 	print(f'Победа игрока {player_1}')
# else:
# 	print(f'Победа игрока {player_2}')


# a) Добавьте игру против бота

# import random

# def input_candies(player):
# 	input_candi = int(input(f"{player}, введите количество конфет, которое возьмете от 1 до 28: "))
# 	while input_candi < 1 or input_candi > 28:
# 		input_candi = int(input("Введите корректное количество конфет: "))
# 	return input_candi

# def input_candies_bot(player):
# 	input_candi = random.randint(1, 28)
# 	print(f'{player} берет {input_candi} конфет')
# 	return input_candi

# def conclusion(player, candies, cand, count):
# 	print(f'Игрок {player}, взял {cand} конфет. Всего у игрока {count} конфет, на столе осталось {candies} конфет')


# candies = 200

# player_1 = input('Введите имя первого игрока: ')
# player_2 = 'Бот'
# print(f'Второй игрок {player_2}')


# turn = random.randint(0, 1)
# if turn == 0:
# 	print(f'Первым ходит {player_1}')
# else:
# 	print(f'Первым ходит {player_2}')

# count_1 = 0
# count_2 = 0

# while candies > 28:
# 	if turn == 0:
# 		cand = input_candies(player_1)
# 		candies -= cand
# 		count_1 += cand
# 		conclusion(player_1, candies, cand, count_1)
# 		turn = 1

# 	else:
# 		cand = input_candies_bot(player_2)
# 		candies -= cand
# 		count_2 += cand
# 		conclusion(player_2, candies, cand, count_2)
# 		turn = 0
# if turn == 0:
# 	print(f'Победа игрока {player_1}')
# else:
# 	print(f'Победа игрока {player_2}')


# b) Подумайте как наделить бота ""интеллектом""


# import random

# def input_candies(player):
# 	input_candi = int(input(f"{player}, введите количество конфет, которое возьмете от 1 до 28: "))
# 	while input_candi < 1 or input_candi > 28:
# 		input_candi = int(input("Введите корректное количество конфет: "))
# 	return input_candi

# def input_candies_bot(player, candies):
# 	input_candi = random.randint(1, 28)
# 	while (candies - input_candi) <= 28 and candies > 29:
# 		input_candi = random.randint(1, 28)
# 	print(f'{player} берет {input_candi} конфет')
# 	return input_candi

# def conclusion(player, candies, cand, count):
# 	print(f'Игрок {player}, взял {cand} конфет. Всего у игрока {count} конфет, на столе осталось {candies} конфет')


# candies = 200

# player_1 = input('Введите имя первого игрока: ')
# player_2 = 'Бот'
# print(f'Второй игрок {player_2}')


# turn = random.randint(0, 1)
# if turn == 0:
# 	print(f'Первым ходит {player_1}')
# else:
# 	print(f'Первым ходит {player_2}')

# count_1 = 0
# count_2 = 0

# while candies > 28:
# 	if turn == 0:
# 		cand = input_candies(player_1)
# 		candies -= cand
# 		count_1 += cand
# 		conclusion(player_1, candies, cand, count_1)
# 		turn = 1

# 	else:
# 		cand = input_candies_bot(player_2, candies)
# 		candies -= cand
# 		count_2 += cand
# 		conclusion(player_2, candies, cand, count_2)
# 		turn = 0
# if turn == 0:
# 	print(f'Победа игрока {player_1}')
# else:
# 	print(f'Победа игрока {player_2}')




# Создайте программу для игры в ""Крестики-нолики"".



# print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)
# board = list(range(1, 10))


# def draw_board(board):
#     print("-" * 13)
#     for i in range(3):
#         print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print("-" * 13)


# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда поставим " + player_token+"? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print("Эта клетка уже занята!")
#         else:
#             print("Некорректный ввод. Введите число от 1 до 9.")


# def check_win(board):
#     win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
#                  (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False


# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print(tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)


# main(board)

# input("Нажмите Enter для выхода!")



# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def encode(f):
	encoding = ""
	i = 0
	while i < len(f):
		count = 1
		while i + 1 < len(f) and f[i] == f[i + 1]:
			count = count + 1
			i = i + 1
		encoding += str(count) + f[i]
		i = i + 1
	return encoding


def decoding(f):
	number = ''
	res = ''
	i = 0
	while i < len(f):
		if not f[i].isalpha():
			number += f[i]
			i = i + 1
		else:
			res = res + f[i] * int(number)
			number = ''
			i = i + 1
	return res


with open('text_1.txt', 'r', encoding='utf-8') as fille:
	fielle_1 = fille.readline()
print(f'Исходная строка: {fielle_1}')
fielle_1 = encode(fielle_1)
print(f'Строка после сжатия: {fielle_1}')
with open('text_2.txt', 'w', encoding='utf-8') as fille:
	fille.write(fielle_1)

print('Восстановление данных')
with open('text_2.txt', 'r', encoding='utf-8') as fille:
	fielle_2 = fille.readline()
print(f'Исходная строка: {fielle_2}')
fielle_2 = decoding(fielle_2)
print(f'Строка после Восстановления: {fielle_2}')





