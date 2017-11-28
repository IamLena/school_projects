# Лабораторная работа на базу данных
# Лучина ИУ7-11
import pickle
data = {}

def search (DATA, par, value):
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
        loop5 = True
        while loop5:
            YesNo = input('Добавить другой(дополнительный) параметр поиска? ')
            if YesNo == 'нет':
                loop5 = False
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
            for i in data:
                print('{:15}'.format(i), end = '')
            print()
            N = len(data)
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
                value1 = input('%s: '%par1)
                s = search(data, par1, value1)
                if s != None:
                    for i in s:
                        print('{:15}'.format(i), end = '')
                    print()
                    for v in range(len(list(s.values())[0])):
                        for i in s:
                            print('{:15}'.format(s[i][v]), end = '')
                        print()

    elif menu == '6':
        if len(data) == 0:
            print('Сначал нужно открыть')

    # else:

    print()
    YesNo = input('Продолжить работу с базой данной? (да/нет) ')
    if YesNo == 'да':
        pass
    elif YesNo == 'нет':
        
        loop = False
    else:
        pass