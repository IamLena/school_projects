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
            return 'ERROR'
    else:
        YesNo = input('Добавить другой (дополнительный) параметр поиска? ')
        if YesNo == 'нет':
            print('SEARCHING')
            print(SearchData)

            return SearchData
        elif YesNo == 'да':
            par2 = input('Введите название параметра:')
            if not (par2 in list(data.keys())):
                print('Данного параметра нет в базе данных')
                return 'ERROR'
            else:
                value2 = input('%s: '%par2)
                s = search(SearchData,par2,value2)
                return s
        else:
            print('Некорректный ввод.')
            return 'ERROR'

data = {'Name':['Bob','Bob','Kate','Sam'],'Age':['3','40','5', '10'],'Sex':['male','male','female','male']}
par1 = input('par: ')
value1 = input('val: ')

#search(data, par1,value1)
print(search(data, par1, value1))