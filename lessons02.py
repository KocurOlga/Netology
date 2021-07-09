HELP = """Доступные команды:
help - напечатать справку
add - добавить задачу
print - распечатать все задачи
exit - выход из программы
"""

today = []
tomorrow = []
other = []
tasks = {'today': today, 'tomorrow': tomorrow, 'other': other}

while True:
    command = input('Введите команду: ')
    if command == 'help':
        print(HELP)
    elif command == 'add':
        task = input('Введите задачу: ')
        data = input('Введите дату задачи (today/tomorrow/other): ')
        if data == 'today':
            today.append(task)
        elif data == 'tomorrow':
            tomorrow.append(task)
        else: other.append(task)
    elif command == 'print':
        print(tasks)
    elif command == 'exit':
        print('Спасибо за использование! До свидания!')
        break
    else: break

print('End')
