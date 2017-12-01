from math import sqrt
def add_dot():
    x, y = map(float,input('координаты: ').split())
    print(M)
    if len(M) == 0:
        M.append([x,y])
    else:
        exist = 0
        for i in range(len(M)):
            if M[i]==[x,y]:
                print('Данная точка уже отмечена')
                exist = 1
        if exist == 0:
            M.append([x,y])
M = []
for i in range(4):
    add_dot()
print(M)
def solve():
    if len(M)<3:
        print('Мало точек.')
    else:
        MaxS = 0
        for i in range(len(M)):
            dot1 = M[i]
            for j in range(i+1, len(M)):
                dot2 = M[j]
                for k in range(j+1, len(M)):
                    dot3 = M[k]
                    print('***',dot1,dot2,dot3)
                    a = sqrt((dot2[0]-dot1[0])**2 + (dot2[1]-dot1[1])**2)
                    b = sqrt((dot1[0]-dot3[0])**2 + (dot1[1]-dot3[1])**2)
                    c = sqrt((dot3[0]-dot2[0])**2 + (dot3[1]-dot2[1])**2)
                    p = (a+b+c)/2
                    S = sqrt(p*(p-a)*(p-b)*(p-c))
                    if S > MaxS:
                        MaxS = S
                        triangle = [dot1,dot2,dot3]
                    print(S)
    print(MaxS,triangle )
    if MaxS == 0:
        return 'Нет решения.'
    else:
        return MaxS, triangle
solve()
    
