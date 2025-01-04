from Usuario import Usuario
from hashlib import sha256
import customtkinter as ctk
from PIL import Image

#Criando e configurando a janela do login
janelaLogin = ctk.CTk(fg_color="White")
janelaLogin._set_appearance_mode("light")
janelaLogin.title("Login")
janelaLogin.geometry("720x400")
janelaLogin.maxsize(width=1920, height=1080)
janelaLogin.minsize(width=720, height=350)


#Label para apresentar a empresa
empresa = ctk.CTkLabel(master=janelaLogin, 
                       text="Seja Bem-Vindo a \nPropriedade Produtiva!", 
                       fg_color="White", 
                       text_color="Black",
                       font=("Arial black", 20)).place(x=50, y=20)

subtitulo = ctk.CTkLabel(master=janelaLogin, 
                         text="A sua empresa mais tecnologica!", 
                         fg_color="White", 
                         text_color="Black",
                         font=("Arial", 15)).place(x=60, y=75)

frame = ctk.CTkFrame(master=janelaLogin,
                     width=350,
                     height=380,
                     corner_radius=20,
                     bg_color="White",
                     fg_color="Gainsboro",
                     border_color="Gainsboro").place(x=360, y=10)

labelLogin = ctk.CTkLabel(master=janelaLogin,
                          text_color="Grey31",
                          text= "Sistema de Login",
                          fg_color="Gainsboro",
                          bg_color="Gainsboro",
                          font= ("ArialBlack", 30)).place(x=420, y=25)

#Criando e configurando os campos de usuario e senha
user = ctk.CTkEntry(master=janelaLogin, 
                    fg_color="lightGreen", 
                    bg_color="Gainsboro",
                    corner_radius=20,
                    width=310,
                    height=37,
                    border_width=3,
                    font=("Arial", 20),
                    placeholder_text="Usuario",
                    placeholder_text_color="Gray").place(x=380, y=150)

senha = ctk.CTkEntry(master=janelaLogin,
                    fg_color="lightGreen", 
                    bg_color="Gainsboro",
                    corner_radius=20,
                    width=310,
                    height=37,
                    border_width=3,
                    font=("Arial", 20),
                    placeholder_text="Senha",
                    placeholder_text_color="Gray").place(x=380, y=220)

logotipo = ctk.CTkImage(light_image=Image.open("./logo.png"),
                        dark_image=Image.open("./logo.png"),
                        size=(341,222))

display_imagem = ctk.CTkLabel(master=janelaLogin,
                              image=logotipo,
                              text="").place(x=10, y=120)

#Criando nova janela
def janelaPrincipal():
    janelaLogin.withdraw()
    janelaP = ctk.CTkToplevel(janelaLogin, fg_color="Gainsboro")
    janelaP.title("Principal")
    janelaP.geometry("1280x720")
    janelaP.maxsize(width=1920, height=1080)
    janelaP.minsize(width=1280, height=720)



Login = ctk.CTkButton(master=janelaLogin, 
                      text="Login",
                      hover_color="LightGreen",
                      fg_color="LightGreen", 
                      bg_color= "Gainsboro",
                      corner_radius=20,
                      text_color="Grey31",
                      font=("ArialBlack", 15),
                      command=janelaPrincipal).place(x=400,y=300)

#Criando e configurando a janela de cadastro


janelaLogin.mainloop()


       