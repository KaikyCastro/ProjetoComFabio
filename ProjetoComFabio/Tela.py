#encoding: utf-8


from hashlib import sha256
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

janelaLogin = ctk.CTk(fg_color="White")

class Login():
    def __init__(self):
        super().__init__()
        self.janelaLogin = janelaLogin
        self.tema()
        self.tela()
        self.tela_login()
        self.janelaLogin.mainloop()

    def returLogin(self):
        return self.loginFrame

    def tema(self):
        self.janelaLogin._set_appearance_mode("light")
        self.janelaLogin.title("Login")
        

    def tela(self):
        #Configurando a janela do login
        self.janelaLogin.geometry("720x400")
        self.janelaLogin.maxsize(width=720, height=400)
        self.janelaLogin.minsize(width=720, height=400)
        self.janelaLogin.iconbitmap("icon.ico")

    def tela_login(self):
        #Label para apresentar a empresa
        self.empresa = ctk.CTkLabel(master=self.janelaLogin, 
                               text="Seja Bem-Vindo a \nPropriedade Produtiva!", 
                               fg_color="White", 
                               text_color="Black",
                               font=("Arial Black", 20))
        self.empresa.place(x=50, y=20)

        self.subtitulo = ctk.CTkLabel(master=self.janelaLogin, 
                                 text="Profissionalize sua Propriedade Rural!", 
                                 fg_color="White", 
                                 text_color="Black",
                                 font=("Arial", 15))
        self.subtitulo.place(x=48, y=75)

        self.loginFrame = ctk.CTkFrame(master=self.janelaLogin,
                             width=350,
                             height=380,
                             corner_radius=20,
                             bg_color="White",
                             fg_color="Gainsboro",
                             border_color="Gainsboro")
        self.loginFrame.place(x=350, y=10)

        self.labelLogin = ctk.CTkLabel(master=self.loginFrame,
                                  text_color="Grey31",
                                  text= "Sistema de Login",
                                  fg_color="Gainsboro",
                                  bg_color="Gainsboro",
                                  font= ("ArialBlack", 30))
        self.labelLogin.place(x=60, y=25)

        #Criando e configurando os campos de usuario e senha
        self.user = ctk.CTkEntry(master=self.loginFrame, 
                            fg_color="lightGreen", 
                            bg_color="Gainsboro",
                            corner_radius=20,
                            width=310,
                            height=37,
                            text_color="Grey31",
                            border_width=3,
                            font=("Arial", 20),
                            placeholder_text="CPF (ex: ***.***.***-**)",
                            placeholder_text_color="Gray")
        self.user.place(x=20, y=100)

        self.senha = ctk.CTkEntry(master=self.loginFrame,
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
        self.senha.place(x=20, y=160)
        
        def visualizarSenha():
            if self.ChekSenha.get() == "on":
                self.senha.configure(show = "")
            else:
                self.senha.configure(show = "*")

        #Checkbox para visualizar senha
        self.ChekSenha = ctk.CTkCheckBox(master=self.loginFrame,
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
                                    command=visualizarSenha,
                                    font=("Arial", 15))
        self.ChekSenha.place(x=30, y=220)
        

        self.logotipo = ctk.CTkImage(light_image=Image.open("./logo.png"),
                                dark_image=Image.open("./logo.png"),
                                size=(341,222))

        self.display_imagem = ctk.CTkLabel(master=self.janelaLogin,
                                      image=self.logotipo,
                                      text="")
        self.display_imagem.place(x=10, y=120)

        def cadastrar():
            self.loginFrame.place_forget()

            self.cadFrame = ctk.CTkFrame(master=self.janelaLogin,
                                    width=350,
                                    height=380,
                                    corner_radius=20,
                                    bg_color="White",
                                    fg_color="Gainsboro",
                                    border_color="Gainsboro")
            self.cadFrame.place(x=350, y=10)

            self.cadLabel = ctk.CTkLabel(master=self.cadFrame,
                                    text_color="Grey31",
                                    text= "Cadastre-se",
                                    fg_color="Gainsboro",
                                    bg_color="Gainsboro",
                                    font= ("ArialBlack", 30))
            self.cadLabel.place(x=88, y=10)

            self.nomeColaborador = ctk.CTkEntry(master=self.cadFrame,
                                           fg_color="lightGreen", 
                                           bg_color="Gainsboro",
                                           corner_radius=20,
                                           width=310,
                                           height=37,
                                           text_color="Grey31",
                                           border_width=3,
                                           font=("Arial", 20),
                                           placeholder_text="Nome Completo",
                                           placeholder_text_color="Gray")
            self.nomeColaborador.place(x=20, y=60)

            self.CPFColaborador = ctk.CTkEntry(master=self.cadFrame,
                                           fg_color="lightGreen", 
                                           bg_color="Gainsboro",
                                           corner_radius=20,
                                           width=310,
                                           height=37,
                                           text_color="Grey31",
                                           border_width=3,
                                           font=("Arial", 20),
                                           placeholder_text="CPF (ex: ***.***.***-**)",
                                           placeholder_text_color="Gray")
            self.CPFColaborador.place(x=20, y=110)

            self.senhaColaborador = ctk.CTkEntry(master=self.cadFrame,
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
            self.senhaColaborador.place(x=20, y=160)

            self.confirmSenha = ctk.CTkEntry(master=self.cadFrame,
                                             fg_color="lightGreen", 
                                             bg_color="Gainsboro",
                                             corner_radius=20,
                                             width=310,
                                             height=37,
                                             text_color="Grey31",
                                             border_width=3,
                                             font=("Arial", 20),
                                             placeholder_text="Confirmar Senha",
                                             show="*",
                                             placeholder_text_color="Gray")
            self.confirmSenha.place(x=20, y=210)

            self.campoObrigatorio = ctk.CTkLabel(master=self.cadFrame,
                                                 text="* Campos obrigatorios",
                                                 text_color="firebrick",
                                                 fg_color="Gainsboro",
                                                 bg_color="Gainsboro",
                                                 font=("Arial", 15))
            self.campoObrigatorio.place(x=20, y=253)

            def visualizarSenhas():
                if self.checkSenhaCad.get() == "on":
                    self.senhaColaborador.configure(show = "")
                    self.confirmSenha.configure(show = "")
                else:
                    self.senhaColaborador.configure(show = "*")
                    self.confirmSenha.configure(show = "*")

            self.checkSenhaCad = ctk.CTkCheckBox(master=self.cadFrame,
                                                 width=10,
                                                height=10,
                                                border_width=3,
                                                bg_color="Gainsboro",
                                                fg_color="Grey31",
                                                hover_color="Gray",
                                                text="Visualizar senhas",
                                                onvalue="on",
                                                offvalue="off",
                                                text_color="Grey31",
                                                command=visualizarSenhas,
                                                font=("Arial", 15))
            self.checkSenhaCad.place(x=180, y=255)
            def voltar():
                self.cadFrame.place_forget()
                self.loginFrame.place(x=350, y=10)

            self.botaoVoltar = ctk.CTkButton(master=self.cadFrame,
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
            self.botaoVoltar.place(x=30, y=300)

            def cadColab():
                self.msg = messagebox.showinfo(title="Cadastro", message="Colaborador cadastrado com sucesso!")
                self.cadFrame.place_forget()
                self.loginFrame.place(x=350, y=10)


            self.botaoCadColab = ctk.CTkButton(master=self.cadFrame,
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
            self.botaoCadColab.place(x=180, y=300)
        #Criando e configurando a janela de cadastro

        self.botaoCadastro = ctk.CTkButton(master=self.loginFrame, 
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
        self.botaoCadastro.place(x=180,y=300)

        def logar():
            self.msg = messagebox.showinfo(title="Login", message="Logado com sucesso!")
            self.janelaLogin.withdraw()
            self.novaTela = ctk.CTkToplevel(fg_color="Gainsboro")
            self.novaTela.title("Propriedade Produtiva")
            self.novaTela.iconbitmap("icon2.ico")
            self.novaTela.geometry("1536x864")
            self.novaTela.minsize(1536, 864)
            self.novaTela.maxsize(1536, 864)
            
            #exibindo nome de quem ta usando o sistema
            self.userNow = ctk.CTkLabel(master=self.novaTela,
                                   text="Bem-vindo, Fulano!",
                                   fg_color="Gainsboro",
                                   text_color="Black",
                                   font=("Arial Black", 20))
            self.userNow.place(x=50, y=20)



            

        self.botaoLogin = ctk.CTkButton(master=self.loginFrame, 
                              text="Login",
                              hover_color="LightGreen",
                              fg_color="LightGreen", 
                              bg_color= "Gainsboro",
                              corner_radius=20,
                              text_color="Grey31",
                              font=("ArialBlack", 15),
                              border_width=3,
                              command=logar,
                              border_color="Grey31")
        self.botaoLogin.place(x=30,y=300)

       