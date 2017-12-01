import math
def func(arg):
    return arg**2

try:
    a, b = map(float, input('a and b: ').split())
    N1 = int(input('N1: '))
    N2 = int(input('N2: '))
except ValueError:
    print('Некорректный ввод1')
    exit()
if N1<=0 or N2<=0:
    print('Некорректный ввод2')
    exit()

print('\u250c','\u2500'*31,'\u252c','\u2500'*21,'\u252c','\u2500'*21,'\u2510', sep = '')
print('\u2502', ' '*31,'\u2502',' N1 = ','{:^15}'.format(N1), '\u2502', ' N2 = ', '{:^15}'.format(N2),'\u2502', sep = '')
print('\u251c', '\u2500'*31, '\u253c', '\u2500'*21, '\u253c', '\u2500'*21, '\u2524', sep = '')

# левые прямоугольники!
def Integral_1(n):
    global a
    global b
    step = (b-a)/n
    I = 0
    if a>b:
        a, b = b, a
    x = a
    while x <= b:
        f = func(x)
        I += f * step
        x += abs(step)
    return I

I1 = round(Integral_1(N1),6)
I2 = round(Integral_1(N2),6)

print('\u2502', 'метод левых прямоугольников    ' ,'\u2502','{:^21}'.format(I1), '\u2502','{:^21}'.format(I2),'\u2502', sep = '')
print('\u251c', '\u2500'*31, '\u253c', '\u2500'*21, '\u253c', '\u2500'*21, '\u2524', sep = '')

# метод симпсона!
def Integral_2 (n):
    global a
    global b
    step = (b-a)/n
    abstep = abs(step)
    I = 0
    if a>b:
        a, b = b, a
    x = a
    while x<=b:
        f1 = func(x)
        f2 = func(x+abstep/2)
        f3 = func(x+abstep)
        I += step/6 * (f1+4*f2+f3)
        x += abstep
    return I

I1 = round(Integral_2(N1),6)
I2 = round(Integral_2(N2),6)

print('\u2502', 'метод симпсона', ' '*17 ,'\u2502','{:^21}'.format(I1), '\u2502', '{:^21}'.format(I2),'\u2502', sep = '')
print('\u2514','\u2500'*31, '\u2534', '\u2500'*21, '\u2534','\u2500'*21,'\u2518', sep = '')

try:
    eps = float(input('Введите точность: '))
except ValueError:
    print('Некорректный ввод3')
    exit()
n = 1
while abs(Integral_1(2*n)-Integral_1(n)) > eps:
    n*=2
print('методом левых прямоугольников данная точность будет достигнута при n, равному ',n)
