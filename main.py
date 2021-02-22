#DESENVOLVIMENTO DE INTERFACES GRÁFICAS
# coding: utf-8


import tkinter #importar a biblioteca Tkinter

janela = tkinter.Tk() #Criar uma janela principal
janela.title('Janela principal') #Dar um titulo para janela

janela['bg'] = 'green' #Dar uma cor para a janela
janela['background'] = 'green'
#LxA+E+T
#300x300+100+100
janela.geometry('800x500+100+100') #Expecificar as dimenções da janela

janela.mainloop() #fechar janela

#todo código do programa deve estar antes deste comando.
