# Лабораторная работа на базу данных
# Лучина ИУ7-11
import pickle
data = {}

def printdb (DATA):
    for i in DATA:
        print('{:15}'.format(i), end = '')
    print()
    N = len(DATA)
    print('\u2500'*15*N)
    for v in range(len(list(DATA.values())[0])):
        for i in DATA:
            print('{:15}'.format(DATA[i][v]), end = '')
        print()

def search (DATA, par, value):
    printdb(DATA)
    k = len(list((DATA.values()))[0])
    count = 0
    SearchData = dict.fromkeys(list(DATA.keys()))
    for key in SearchData:
        SearchData[key] = []
    for n in range(k):
        if DATA[par][n] == value:
            for i in DATA:
                SearchData[i].append(DATA[i][n])
                count = 1
    if count == 0:
            print('Такого элемента нет в базе данных.')
            return None
    else:
        YesNo = input('Добавить другой (дополнительный) параметр поиска? ')
        if YesNo == 'нет':
            return SearchData
        elif YesNo == 'да':
            par2 = input('Введите название параметра:')
            if not (par2 in list(data.keys())):
                print('Данного параметра нет в базе данных')
            else:
                value2 = input('%s: '%par2)
                search(SearchData,par2,value2)
        else:
            print('Некорректный ввод.')
        printdb(SearchData)


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
        if columns <=0:
            print('Создание такой базы данных невозможно.')
        else:
            keys = []
            for i in range(columns):
                key = input('Введите название %d-го парметра: '%(i+1))
                keys.append(key)
            NewData = dict.fromkeys(keys)
            for i in NewData:
                    NewData[i] = []
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
            printdb(NewData)
            p = pickle.dumps(NewData)
            file = input('Назовите базу данных: ')
            file += '.mybd'
            with open(file, 'wb') as f:
                f.write(p)
            print('База Данных создана. Имя файла - ', file)

    elif menu == '2':
        file = input('Введите имя файла, в котором хранится база данных: ')
        if (file[-5:]) != '.mybd':
            print('Не то разрешение файла')
        else:
            try:
                with open(file,'br') as f:
                    data = pickle.loads(f.read())
                print('Файл открыт.')
            except FileNotFoundError:
                print('Файл с данным именем не найден.')

    elif menu == '3':
        if len(data) == 0:
            print('Сначала откройте нужную базу данных.')
        else:
            printdb(data)
            
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
            printdb(data)

    elif menu == '5':
        if len(data) == 0:
            print('Сначала откройте нужную базу данных.')
        else:
            par1 = input('Введите название параметра: ')
            if not (par1 in list(data.keys())):
                print('Данного параметра нет в базе данных')
            else:
                value1 = input('%s: '%par1)
                s = search(data, par1, value1)
                printdb(s)

    elif menu == '6':
        if len(data) == 0:
            print('Сначал откройте нужную базу данных.')
        else:
            par1 = input('Введите параметр поиска элемента для удаления: ')
            if not (par1 in list(data.keys())):
                print('Данного параметра нет в базе данных')
            else:
                value1 = input('%s: '%par1)
                s = search(data, par1, value1)
                printdb(s)
            

    # else:

    print()
    YesNo = input('Продолжить работу с базой данной? (да/нет) ')
    if YesNo == 'да':
        pass
    elif YesNo == 'нет':
        
        loop = False
    else:
        pass