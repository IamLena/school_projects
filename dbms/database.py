# Лабораторная работа на базу данных
# Лучина ИУ7-11
import pickle
data = 'None'
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
    print()

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
                elif YesNo == 'нет':
                    loop1 = False
                    loop11 = False
                else:
                    print('Некорректный ввод. Попробуйте ещё раз.')
        print(NewData)
        p = pickle.dumps(NewData)
        file = input('Назовите базу данных: ')
        file += '.mybd'
        with open(file, 'wb') as f:
            f.write(p)
        print('База Данных создана. Имя файла - ', file)

    elif menu == '2':
        file = input('Введите имя файла, в котором хранится база данных: ')
        if file == '':
            file = 'luch.mybd'
        if (file[-5:]) != '.mybd':
            print('Не то разрешение файла')
        else:
            try:
                f = open(file,'br')
                data = pickle.loads(f.read())
                f.close()
                print('Файл открыт.')
            except FileNotFoundError:
                print('Файл с данным именем не найден.')

    elif menu == '3':
        if data == 'None':
            print('Сначала откройте нужную базу данных.')
        else:
            N = len(data)
            for i in data:
                print('{:15}'.format(i), end = '')
            print()
            print('\u2500'*15*N)
            n = len(list(data.values())[0])
            for j in range(n):
                for i in data:
                    e = data[i][j]
                    print('{:15}'.format(e), end = '')
                print()
            
    # elif menu == '4':
    # elif menu == '5':
    # elif menu == '6':
    # else:

    print()
    YesNo = input('Продолжить редактирование? (да/нет) ')
    if YesNo == 'да':
        pass
    elif YesNo == 'нет':
        print('СОХРАНИТЬ')
        loop = False
    else:
        pass