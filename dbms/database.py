# Лабораторная работа на базу данных
# Лучина ИУ7-11
loop = True
while loop:
    print('{:_^40}'.format('MENU'))
    print('1 - создать базу данных')
    print('2 - открыть базу данных')
    print('3 - просмотреть все элементы базы данных')
    print('4 - добавить новый элемент в базу данных')
    print('5 - найти элемент базы данных')
    print('6 - удалить элемент из базы данных')
    menu = input('Введите пунк меню: ')
    DATA = dict.fromkeys(['Имя','Фамилия','Пол','Возраст'])
    print(DATA)
    DATA['Имя'] = ['Петя','Вася','Катя']
    DATA['Фамилия'] = ['Петров','Васечкин','Иванова']
    DATA['Пол'] = ['м','м','ж']
    DATA['Возраст'] = [15,10,40]
    print(DATA)
    n = 3
    for j in range(n):
        for i in DATA:
            print(DATA[i][j], end = ' ')
        print()
    
    loop = False

    #if menu == '1':
    # elif menu == '2':
    # elif menu == '3':
    # elif menu == '4':
    # elif menu == '5':
    # elif menu == '6':
    # else:

