# Лабораторная работа на базу данных
# Лучина ИУ7-11
import pickle
data = {}

loop = True
while loop:
    print('{:_^40}'.format('MENU'))
    print('1 - создать базу данных')
    print('2 - открыть базу данных')
    print('3 - просмотреть все элементы базы данных')
    print('4 - добавить новые элементы в базу данных')
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
        if len(data) == 0:
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
            
    elif menu == '4':
        if len(data) == 0:
            print('Сначала откройте нужную базу данных.')
        else:
            for i in data:
                value = input('%s: '%i)
                data[i].append(value)
        loop1 = True
        while loop1:
            loop11 = True
            while loop11:
                YesNo = input('Добавить еще запись?(да/нет) ')
                if YesNo == 'да':
                    for i in data:
                        value = input('%s: '%i)
                        data[i].append(value)
                    loop11 = False
                elif YesNo == 'нет':
                    loop1 = False
                    loop11 = False
                else:
                    print('Некорректный ввод. Попробуйте ещё раз.')

    elif menu == '5':
        if len(data) == 0:
            print('Сначала откройте нужную базу данных.')
        else:
            par1 = input('Введите название параметра: ')
            if not (par1 in list(data.keys())):
                print('Данного параметра нет в базе данных')
            else:
                value = input('Введите значение: ')
                k = len(list((data.values()))[0])
                for n in range(k):
                    if data[par1][n] == value:
                        for i in data:
                            print('{:15}'.format(i), end = '')
                        print()
                        for i in data:
                            print('{:15}'.format(data[i][n]), end = '')


            # search = int(input('По какому количеству параметров осуществлять поиск?'))
            # pars = []
            # for i in range(search):
            #     par = input('Введите параметр: ')
            #     if not (par in list(data.keys())):
            #         print('В базе данных нет такого параметра.')
            #     pars.append(par)
            # values = []
            # for p in pars:
            #     value = input('%s: '%p)
            #     values.append(value)
            # print(pars, values)
            # ID = -1
            # n = len(list(data.values())[0])

            # for i in range(n):
            #     if data[pars[0]][i] == values[0]:
            #         if search > 1:
            #             if data[pars[1]][i] == values[1]:
            #                 ID = i        
            #         else:
            #             ID = i

            # if ID != -1:
            #     N = len(data)
            #     for d in data:
            #         print('{:15}'.format(d), end = '')
            #     print()
            #     print('\u2500'*15*N)
            #     for o in data:
            #         e = data[o][ID]
            #         print('{:15}'.format(e), end = '')  
            # else:
            #     print('Элемент не найден')

                

    # elif menu == '6':
    # else:

    print()
    YesNo = input('Продолжить работу с базой данной? (да/нет) ')
    if YesNo == 'да':
        pass
    elif YesNo == 'нет':
        
        loop = False
    else:
        pass