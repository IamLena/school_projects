# import tkinter
# tkinter._test()
from tkinter import *
root = Tk()
def hello(event):
    print('hello world!')
ed = Entry(root, width = 20)
add_btn = Button(root, text = 'add a dot', width = 8, height = 1, bg = 'black', fg = 'white')
solve_btn = Button(root, text = 'solve', width = 20, height = 1, bg = 'black', fg = 'white')
delete_btn = Button(root, text = 'clear', width = 8, height = 1, bg = 'black', fg = 'white')
add_btn.bind("<Button-1>", hello)
ed.grid(row = 1, column = 1)
add_btn.grid(row = 1, column = 2)
solve_btn.grid(row = 2, column = 1)
delete_btn.grid(row = 2, column = 2)
root.mainloop()