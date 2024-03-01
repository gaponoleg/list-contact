def edit_cont():
    name = str(input('Введите индекс контакта: '))
    rename = str(input('Перепешите'))
    with open('info.txt') as data:
        lines = data.readlines()
        print(lines)
        b = False
        for line in lines:
            if serch.lower() in line.lower():

                b = True
        if b == False:
            print('Такого контакта нет или неправильно указано фио')
    menu()
def copy():
    with open('info.txt') as source, open('output.txt', 'w') as destination:
        for line in source:
            destination.write(line)
    menu()
def del_cont():
    name = str(input('Введите индекс контакта: '))
    name_int = int(name)

    with open('info.txt') as data:
        lines = data.readlines()
        b = False
        for line in lines:
            if name.lower() in line.lower():
                with open('info.txt', 'w') as file:
                    del lines[name_int-1]
                    print('Контакт удалён')
                    for i in range(len(lines)):
                        file.write(lines[i][3:])
                    b == True
        if b == False:
            print('Такого контакта нет или неправильно указано фио')
    with open('info.txt', 'r') as f:
        lines = f.readlines()

    with open('info.txt', 'w') as f:
        for i, line in enumerate(lines, 1):
            if f'{i}:' not in line:
                f.write(f'{i}: {line}')
            else:
                f.write(line)
    menu()

def add_cont():
    info = (str(input('Введите фио и номер телефона через пробел: ')))
    info.split()
    with open('info.txt', 'a') as data:
        data.writelines(f'{info}\n')

    with open('info.txt', 'r') as f:
        lines = f.readlines()

    with open('info.txt', 'w') as f:
        for i, line in enumerate(lines, 1):
            if f'{i}:' not in line:
                f.write(f'{i}: {line}')
            else:
                f.write(line)
    menu()

def check_cont():
    data = open('info.txt', 'r')
    for i in data:
        print(i)
    menu()

def serch():
    serch = str(input('Введите имя фамилию очество или номер телефона для поиска контакта: '))
    with open('info.txt') as data:
        lines = data.readlines()
        b = False
        for line in lines:
            if serch.lower() in line.lower():
                print(line, end=' ')
                b = True
        if b == False:
            print('Такого контакта нет или неправильно указано фио')
    menu()


def menu():
    print('1. Посмотреть все контакты\n'
          '2. Поиск (напишите имя или фамилию или отчество номер\n '
          'телефона номер телефона)\n'
          '3. Добавить контакт\n'
          '4. Удалить контакт\n'
          '5. Копия контакотов'
          'Напишите exit что бы выйти из программы')
    num = str(input('Выберете функцию: '))
    if num == '1': check_cont()
    if num == '2': serch()
    if num == '3': add_cont()
    if num == '4': del_cont()
    if num == '5': copy()
    if num == 'exit': exit()
menu()
