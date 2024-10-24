from pydoc import plain
from tkinter import Button, PhotoImage

from customtkinter import *
from PIL import Image
### Cores
cinza_escuro = "#1E1E1E"
branco = "#fff"

### Janela
janela = CTk()
janela.geometry("900x600")
janela.resizable(False,False)
janela._set_appearance_mode("dark")

### Imagem de fundo
criar_imagem_fundo = CTkImage(
    dark_image=Image.open("assets/login/imagem_fundo.png"),
    light_image=Image.open("assets/login/imagem_fundo.png"),
    size=(900, 600))
lbl_imagem_fundo = CTkLabel(
    janela,
    image=criar_imagem_fundo,
    text="")
lbl_imagem_fundo.place(x=0,y=0)

### Fundo login
fundo_login = CTkFrame(
    janela,
    height=900,
    width=400,
    fg_color=cinza_escuro,
    bg_color=cinza_escuro)
fundo_login.place(x=500,y=0)

lbl_entrar = CTkLabel(
    janela,
    text="Entrar",
    fg_color=cinza_escuro,
    bg_color=cinza_escuro,
    text_color=branco,
    font=("Roboto Bold", 48 * -1, "bold"),
)
lbl_entrar.place(x=635,y=73)


janela.mainloop()