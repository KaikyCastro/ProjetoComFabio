from Usuario import Usuario
from hashlib import sha256
import customtkinter as ctk
from PIL import Image

#Criando e configurando a janela do login
janelaLogin = ctk.CTk(fg_color="Gainsboro")
janelaLogin._set_appearance_mode("light")
janelaLogin.title("Login")
janelaLogin.geometry("720x400")
janelaLogin.maxsize(width=1920, height=1080)
janelaLogin.minsize(width=720, height=350)


#Label para apresentar a empresa
empresa = ctk.CTkLabel(master=janelaLogin, 
                       text="Seja Bem-Vindo a Propriedade Produtiva!", 
                       fg_color="Gainsboro", 
                       text_color="DarkOliveGreen",
                       font=("Arial black", 20)).pack()

subtitulo = ctk.CTkLabel(master=janelaLogin, 
                         text="A sua empresa mais tecnologica!", 
                         fg_color="Gainsboro", 
                         text_color="DarkOliveGreen",
                         font=("Arial", 15)).pack()


#Criando e configurando os campos de usuario e senha
user = ctk.CTkEntry(master=janelaLogin, 
                    fg_color="lightGreen", 
                    bg_color="Gainsboro",
                    corner_radius=20,
                    width=250,
                    height=50,
                    placeholder_text="Usuario").place(x=450, y=150)

senha = ctk.CTkEntry(master=janelaLogin,
                    fg_color="lightGreen", 
                    bg_color="Gainsboro",
                    corner_radius=20,
                    width=250,
                    height=50,
                    placeholder_text="Senha").place(x=450, y=220)

#Criando nova janela
def janelaPrincipal():
    janelaLogin.withdraw()
    janelaP = ctk.CTkToplevel(janelaLogin, fg_color="white")
    janelaP.title("Principal")
    janelaP.geometry("1280x720")
    janelaP.maxsize(width=1920, height=1080)
    janelaP.minsize(width=1280, height=720)



Login = ctk.CTkButton(master=janelaLogin, text="Login", fg_color="#40E0D0", bg_color= "white", command=janelaPrincipal).pack()

janelaLogin.mainloop()


       