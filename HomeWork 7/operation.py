import csv
import view
import log

def add_сontact(surname, name, tel, description):
	add = [surname, name, tel, description]
	with open('book.csv', 'a', encoding='utf-8') as file:
		writer = csv.writer(file, delimiter=';', lineterminator='\n')
		writer.writerow(add)
	log.log_record('Добавление нового контакта', add)

def view_contact():
	with open('book.csv', 'r', encoding='utf-8') as file:
		conclusion = csv.reader(file, delimiter=';')
		for row in conclusion:
			view.view_contact_console(row[0], row[1], row[2], row[3])
	log.log_record('Просмотр всех контактов')

def find_contact():
	find_surname = view.find_contact_console()
	with open('book.csv', 'r', encoding='utf-8') as file:
		conclusion = csv.reader(file, delimiter=';')
		for row in conclusion:
			if find_surname in row:
				view.view_contact_console(row[0], row[1], row[2], row[3])
	log.log_record('Поиск контакта с фамилией', find_surname)
