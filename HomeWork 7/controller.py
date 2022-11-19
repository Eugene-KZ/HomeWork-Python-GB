
import view
import operation

def start():
	opc = view.menu()
	if opc == '1':
		some_str = view.add_сontact_console()
		operation.add_сontact(some_str[0], some_str[1], some_str[2], some_str[3])
	elif opc == '2':
		operation.view_contact()
	elif opc == '3':
		operation.find_contact()
	else:
		view.error_op()