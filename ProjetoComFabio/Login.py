from hashlib import sha256
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

janelaLogin = ctk.CTk(fg_color="White")

class Login():
    def __init__(self):
        self.janelaLogin = janelaLogin
        self.tema()
        self.tela()
        self.tela_login()
        self.janelaLogin.mainloop()

    def tema(self):
        self.janelaLogin._set_appearance_mode("light")
        self.janelaLogin.title("Login")

    def tela(self):
        #Configurando a janela do login
        
        self.janelaLogin.geometry("720x400")
        self.janelaLogin.maxsize(width=1920, height=1080)
        self.janelaLogin.minsize(width=720, height=350)
        self.janelaLogin.iconbitmap("icon.ico")

    def tela_login(self):

        #Label para apresentar a empresa
        empresa = ctk.CTkLabel(master=self.janelaLogin, 
                               text="Seja Bem-Vindo a \nPropriedade Produtiva!", 
                               fg_color="White", 
                               text_color="Black",
                               font=("Arial black", 20))
        empresa.place(x=50, y=20)

        subtitulo = ctk.CTkLabel(master=self.janelaLogin, 
                                 text="Profissionalize sua Propriedade Rural!", 
                                 fg_color="White", 
                                 text_color="Black",
                                 font=("Arial", 15))
        subtitulo.place(x=48, y=75)

        loginFrame = ctk.CTkFrame(master=self.janelaLogin,
                             width=350,
                             height=380,
                             corner_radius=20,
                             bg_color="White",
                             fg_color="Gainsboro",
                             border_color="Gainsboro")
        loginFrame.place(x=350, y=10)

        labelLogin = ctk.CTkLabel(master=loginFrame,
                                  text_color="Grey31",
                                  text= "Sistema de Login",
                                  fg_color="Gainsboro",
                                  bg_color="Gainsboro",
                                  font= ("ArialBlack", 30))
        labelLogin.place(x=60, y=25)

        #Criando e configurando os campos de usuario e senha
        user = ctk.CTkEntry(master=loginFrame, 
                            fg_color="lightGreen", 
                            bg_color="Gainsboro",
                            corner_radius=20,
                            width=310,
                            height=37,
                            text_color="Grey31",
                            border_width=3,
                            font=("Arial", 20),
                            placeholder_text="CPF",
                            placeholder_text_color="Gray")
        user.place(x=20, y=100)

        senha = ctk.CTkEntry(master=loginFrame,
                            fg_color="lightGreen", 
                            bg_color="Gainsboro",
                            corner_radius=20,
                            width=310,
                            height=37,
                            text_color="Grey31",
                            border_width=3,
                            font=("Arial", 20),
                            placeholder_text="Senha",
                            show="*",
                            placeholder_text_color="Gray")
        senha.place(x=20, y=160)
        
        #Checkbox para visualizar senha
        ChekSenha = ctk.CTkCheckBox(master=loginFrame,
                                    width=10,
                                    height=10,
                                    border_width=3,
                                    bg_color="Gainsboro",
                                    fg_color="Grey31",
                                    hover_color="Gray",
                                    text="Visualizar senha",
                                    onvalue="on",
                                    offvalue="off",
                                    text_color="Grey31",
                                    font=("Arial", 15))
        ChekSenha.place(x=30, y=220)
        

        logotipo = ctk.CTkImage(light_image=Image.open("./logo.png"),
                                dark_image=Image.open("./logo.png"),
                                size=(341,222))

        display_imagem = ctk.CTkLabel(master=self.janelaLogin,
                                      image=logotipo,
                                      text="")
        display_imagem.place(x=10, y=120)

        def janelaPrincipal():
            msgLogin = messagebox.showinfo(title="Login", message="Login efetuado com sucesso!")
            self.janelaLogin.withdraw()
            janelaP = ctk.CTkToplevel(self.janelaLogin, fg_color="Gainsboro")
            janelaP.title("Principal")
            janelaP.geometry("1280x720")
            janelaP.maxsize(width=1920, height=1080)
            janelaP.minsize(width=1280, height=720)


        botaoLogin = ctk.CTkButton(master=loginFrame, 
                              text="Login",
                              hover_color="LightGreen",
                              fg_color="LightGreen", 
                              bg_color= "Gainsboro",
                              corner_radius=20,
                              text_color="Grey31",
                              font=("ArialBlack", 15),
                              border_width=3,
                              border_color="Grey31",
                              command=janelaPrincipal)
        botaoLogin.place(x=30,y=300)

        def cadastrar():
            loginFrame.place_forget()

            cadFrame = ctk.CTkFrame(master=self.janelaLogin,
                                    width=350,
                                    height=380,
                                    corner_radius=20,
                                    bg_color="White",
                                    fg_color="Gainsboro",
                                    border_color="Gainsboro")
            cadFrame.place(x=350, y=10)

            cadLabel = ctk.CTkLabel(master=cadFrame,
                                    text_color="Grey31",
                                    text= "Cadastre o colaborador",
                                    fg_color="Gainsboro",
                                    bg_color="Gainsboro",
                                    font= ("ArialBlack", 30))
            cadLabel.place(x=13, y=10)

            nomeColaborador = ctk.CTkEntry(master=cadFrame,
                                           fg_color="lightGreen", 
                                           bg_color="Gainsboro",
                                           corner_radius=20,
                                           width=310,
                                           height=37,
                                           text_color="Grey31",
                                           border_width=3,
                                           font=("Arial", 20),
                                           placeholder_text="Nome",
                                           placeholder_text_color="Gray")
            nomeColaborador.place(x=20, y=80)

            CPFColaborador = ctk.CTkEntry(master=cadFrame,
                                           fg_color="lightGreen", 
                                           bg_color="Gainsboro",
                                           corner_radius=20,
                                           width=310,
                                           height=37,
                                           text_color="Grey31",
                                           border_width=3,
                                           font=("Arial", 20),
                                           placeholder_text="CPF",
                                           placeholder_text_color="Gray")
            CPFColaborador.place(x=20, y=140)

            menuOpcao = ctk.CTkOptionMenu(master=cadFrame,
                                          values=["Administrador", "Colaborador", "Pilantra", "Fabio"],
                                            fg_color="lightGreen",
                                            bg_color="Gainsboro",
                                            corner_radius=20,
                                            width=310,
                                            height=37,
                                            text_color="Grey31",
                                            font=("Arial", 20))
            menuOpcao.place(x=20, y=250)
            cargoColaborador = ctk.CTkEntry(master=cadFrame,
                                           fg_color="lightGreen", 
                                           bg_color="Gainsboro",
                                           corner_radius=20,
                                           width=310,
                                           height=37,
                                           text_color="Grey31",
                                           border_width=3,
                                           font=("Arial", 20),
                                           placeholder_text="Cargo",
                                           placeholder_text_color="Gray")
            cargoColaborador.place(x=20, y=200)
            
            def voltar():
                cadFrame.place_forget()
                loginFrame.place(x=350, y=10)

            botaoVoltar = ctk.CTkButton(master=cadFrame,
                                        text="Voltar",
                                        hover_color="LightGreen",
                                        fg_color="LightGreen", 
                                        bg_color= "Gainsboro",
                                        corner_radius=20,
                                        text_color="Grey31",
                                        font=("ArialBlack", 15),
                                        border_width=3,
                                        border_color="Grey31",
                                        command=voltar)
            botaoVoltar.place(x=30, y=300)

            def cadColab():
                msg = messagebox.showinfo(title="Cadastro", message="Colaborador cadastrado com sucesso!")
                cadFrame.place_forget()
                loginFrame.place(x=350, y=10)


            botaoCadColab = ctk.CTkButton(master=cadFrame,
                                         text="Cadastrar",
                                         hover_color="LightGreen",
                                         fg_color="LightGreen", 
                                         bg_color= "Gainsboro",
                                         corner_radius=20,
                                         text_color="Grey31",
                                         font=("ArialBlack", 15),
                                         border_width=3,
                                         border_color="Grey31",
                                         command=cadColab)
            botaoCadColab.place(x=180, y=300)
        #Criando e configurando a janela de cadastro

        botaoCadastro = ctk.CTkButton(master=loginFrame, 
                                 text="Cadastrar",
                                 hover_color="LightGreen",
                                 fg_color="LightGreen", 
                                 bg_color= "Gainsboro",
                                 corner_radius=20,
                                 text_color="Grey31",
                                 command=cadastrar,
                                 border_width=3,
                                 border_color="Grey31",
                                 font=("ArialBlack", 15))
        botaoCadastro.place(x=180,y=300)
    

       