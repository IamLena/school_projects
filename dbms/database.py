# Лабораторная работа на базу данных
# Лучина ИУ7-11
import pickle
DATA = dict.fromkeys(['Имя','Фамилия','Пол','Возраст'])

# def create_elements (data):
#     lp = True
#     while lp:
#         lp2 = True
#         while lp2:
#             yn = input('Добавить запись?(да/нет) ')
#             if yn == 'да':
#                 for i in data:
#                     value = input('%s: '%i)
#                     data[i].append(value)
#                 lp2 = False
#             elif yn == 'нет':
#                 lp = False
#                 lp2 = False
#             else:
#                 print('Некорректный ввод. Попробуйте ещё раз.')
#     print(data)
#     return data
# for i in DATA:
#     DATA[i] = []
# create_elements(DATA)

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

    if menu == '1':
        columns = int(input('Введите количество параметров: '))
        keys = []
        for i in range(columns):
            key = input('Введите название %d-го парметра: '%(i+1))
            keys.append(key)
        NewData = dict.fromkeys(keys)
        for i in NewData:
                NewData[i] = []
        print(NewData)
        loop1 = True
        while loop1:
            loop11 = True
            while loop11:
                YesNo = input('Добавить запись?(да/нет) ')
                if YesNo == 'да':
                    for i in NewData:
                        value = input('%s: '%i)
                        NewData[i].append(value)
                    loop11 = False
                if YesNo == 'нет':
                    loop1 = False
                    loop11 = False
                else:
                    print('Некорректный ввод. Попробуйте ещё раз.')
        print(NewData)
        p = pickle.dumps(NewData)
        file = input('Введите имя файла, куда сохранить созданную бд: ')
        with open(file, 'wb') as f:
            f.write(p)
        print('done')

    # elif menu == '2':
    # elif menu == '3':
    # elif menu == '4':
    # elif menu == '5':
    # elif menu == '6':
    # else:

    loop = False