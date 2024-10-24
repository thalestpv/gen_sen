from tkinter import Button

from customtkinter import *

def clique_aqui():
    print("botao")

janela = CTk()
janela.geometry("400x400")
janela.resizable(False,False)
janela._set_appearance_mode("dark")

CTkButton(janela, command=clique_aqui, text="clique aqui").pack()


janela.mainloop()