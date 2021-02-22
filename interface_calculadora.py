from tkinter import *

def bt_enter():
    enter = int(num.get())

    for c in range(1, enter+1):
             lb_res = Label(janela, text=f'{enter} X 0 = {enter*0}\n'
                                    f'{enter} X 1 = {enter*1}\n'
                                    f'{enter} X 2 = {enter*2}\n'
                                    f'{enter} X 3 = {enter*3}\n'
                                    f'{enter} X 4 = {enter*4}\n'
                                    f'{enter} X 5 = {enter*5}\n'
                                    f'{enter} X 6 = {enter*6}\n'
                                    f'{enter} X 6 = {enter*6}\n'
                                    f'{enter} X 7 = {enter*7}\n'
                                    f'{enter} X 8 = {enter*8}\n'
                                    f'{enter} X 9 = {enter*9}\n'
                                    f'{enter} X 10 = {enter*10}', font='vendana').grid(row=1, column=1)


janela = Tk()
janela.title('SUA TABUADA VIRTUAL')

lb = Label(janela, text='Tabuada do:', font='verdana 10 bold').grid(row=1, column=0)

num = Entry(janela, width=10)
num.grid(row=2, column=0)

bt = Button(janela, text='Calcular', width=15, bg='gray', command=bt_enter).grid(row=3, column=0)



janela.geometry('400x300+300+300')
janela.mainloop()