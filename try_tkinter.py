from tkinter import *
from math import sqrt
root = Tk()

#definition
def add_dot(event):
    x = inputx.get()
    y = inputy.get()
    inputx.delete(0,END)
    inputy.delete(0,END)
    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print('That is not a float')
    else:
        if len(M) == 0:
            M.append([x,y])
        else:
            exist = 0
            for i in range(len(M)):
                if M[i]==[x,y]:
                    print('It has been already added')
                    exist = 1
            if exist == 0:
                M.append([x,y])
        print(M)

def solve(event):
    print('solving')
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
                    print(dot1,dot2,dot3)
                    a = sqrt((dot2[0]-dot1[0])**2 + (dot2[1]-dot1[1])**2)
                    b = sqrt((dot1[0]-dot3[0])**2 + (dot1[1]-dot3[1])**2)
                    c = sqrt((dot3[0]-dot2[0])**2 + (dot3[1]-dot2[1])**2)
                    p = (a+b+c)/2
                    S = sqrt(p*(p-a)*(p-b)*(p-c))
                    print(S)
                    if S > MaxS:
                        MaxS = S
                        triangle = [dot1,dot2,dot3]
        if MaxS == 0:
            return 'Нет решения.'
        else:
            print(MaxS, triangle)
            w.create_polygon(triangle[0], triangle[1], triangle[2])

#buttons
inputx = Entry(root, width = 10)
inputy = Entry(root, width = 10)
add_btn = Button(root, text = 'add a dot', width = 8, height = 1, bg = 'black', fg = 'white')
solve_btn = Button(root, text = 'solve', width = 20, height = 1, bg = 'black', fg = 'white')
delete_btn = Button(root, text = 'clear', width = 8, height = 1, bg = 'black', fg = 'white')
w = Canvas(root,width = 200, height = 200)

#packer
inputx.grid(row = 1, column = 1)
inputy.grid(row = 1, column = 2)
add_btn.grid(row = 1, column = 3)
solve_btn.grid(row = 2,column = 1, columnspan = 2)
delete_btn.grid(row = 2, column = 3)
w.grid(row = 3, column = 1, columnspan = 3)

#run
M =[]
add_btn.bind("<Button-1>", add_dot)
add_btn.bind("<Return>", add_dot)
solve_btn.bind('<Button-1>', solve)

root.mainloop()