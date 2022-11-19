

def menu():
	operation = input('Выберите операцию, которую хотите сделать: \n 1: Записать контакт в книгу. \n 2: Посмтреть всю книгу контактов. \n 3: Произвести поиск по фамилии. \nВаш выбор: ')
	return operation

def add_сontact_console():
	surname = input('Введите фамилию: ')
	name = input('Введите имя: ')
	tel = input('Введите номер телефона: ')
	description = input('Введите описание: ')
	return surname, name, tel, description

def view_contact_console(surname, name, tel, description):
	print(f'\nФамилия: {surname} \nИмя: {name} \nТелефон: {tel} \nОписание: {description}')

def find_contact_console():
	surname = input('Введите искомую фамилию: ')
	return surname

def error_op():
	print('Ошибка!!!')

