from tkinter import *
import sqlite3


janela=Tk()
janela.title("Apoio de Idosos")
janela.geometry('800x600')

texto_1 = Label (janela, text='Apoio para Idosos', bg="black",fg = 'white', font = ('arial bold', 20))
texto_1.grid(row=0, column= 0, columnspan=3, pady=20, padx=10)

texto_2=Label (janela, text='')
texto_2.place(x=420, y= 20)
texto_3=Label (janela, text='')
texto_3.place(x=420, y= 80)
texto_4=Label (janela, text='')
texto_4.place(x=420, y= 140)
texto_5=Label (janela, text='')
texto_5.place(x=15, y= 420)

def entry1():
    global texto_5
    nome_v = entrada.get().strip()
    if nome_v == "": return
    
    
    conn = sqlite3.connect('pontuacoes_dos_terceira_idade.db')
    cursor = conn.cursor()
    cursor.execute("SELECT jogo1, jogo2, jogo3 FROM usuarios WHERE nome = ?", (nome_v,))
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        texto_2.configure(text = f'{resultado[0]} Pontos!', font = ('arial bold', 15))
        texto_3.configure(text = f'{resultado[1]} Pontos!', font = ('arial bold', 15))
        texto_4.configure(text = f'{resultado[2]} Pontos!', font = ('arial bold', 15))
        texto_5.configure(text='Seu nome foi verificado!', font = ('arial bold', 15), fg="green")
    else:
        texto_5.configure(text='Usuário não encontrado', font = ('arial bold', 15), fg="red")

def game1():
    global entrada
    entrada = Entry(janela, width=30)
    entrada.place(x=15, y=330)
    texto_3_inst = Label(janela, text='Escreva seu nome para participar:')
    texto_3_inst.place(x=15, y=310)
    botao_conf = Button(janela, text='Confirmar', command = entry1, font=('arial bold', 14), width=15)
    botao_conf.place(x=15,y=360)

botao_1 = Button(janela, text='Jogo 1', command = game1, font = ('arial bold', 14), width= 10) 
botao_1.grid(row=10, column = 0, pady = 10, padx=15)
botao_2 = Button(janela, text='Jogo 2',command = game1, font = ('arial bold', 14),  width= 10)
botao_2.grid(row=20, column = 0, pady= 15)
botao_3 = Button(janela, text='Jogo 3',command = game1, font = ('arial bold', 14), width= 10)
botao_3.grid(row=30, column = 0, pady = 15)


Label(janela, text='Pontuação:', font=('arial bold', 14)).grid(row=10, column=1)
Label(janela, text='Pontuação:', font=('arial bold', 14)).grid(row=20, column=1)
Label(janela, text='Pontuação:', font=('arial bold', 14)).grid(row=30, column=1)

frame_1 = Frame (janela, width=7, height=600, bg='black')
frame_1.place(x=400, y=0)
frame_2 = Frame (janela, width=600, height=7, bg='black')
frame_2.place(x=400, y=200)
frame_3 = Frame (janela, width=500, height=600, bg='black')
frame_3.place(x=400, y=200)

janela.mainloop()