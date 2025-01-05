from Login import *

janelaLogin = Login()
def iniciaTelaPrincipal(self):
    self.janelaPrincipal = ctk.CTkToplevel(master=janelaLogin, fg_color="white")

botaoLogin = ctk.CTkButton(master=janelaLogin.loginFrame, 
                              text="Login",
                              hover_color="LightGreen",
                              fg_color="LightGreen", 
                              bg_color= "Gainsboro",
                              corner_radius=20,
                              text_color="Grey31",
                              font=("ArialBlack", 15),
                              border_width=3,
                              border_color="Grey31",
                              command=iniciaTelaPrincipal)
botaoLogin.place(x=30,y=300)


def janelaPrincipal(self):
            self.msgLogin = messagebox.showinfo(title="Login", message="Login efetuado com sucesso!")
            self.janelaLogin.withdraw()
            self.janelaP = ctk.CTkToplevel(self.janelaLogin, fg_color="Gainsboro")
            self.janelaP.title("Principal")
            self.janelaP.geometry("1280x720")
            self.janelaP.maxsize(width=1920, height=1080)
            self.janelaP.minsize(width=1280, height=720)


class TelaPrincipal(Login):
    def __init__(self):
        super().__init__()
        self.janelaPrincipal = iniciaTelaPrincipal()
        self.configTela()
        self.telaP()
        self.janelaPrincipal.mainloop()

    def configTela(self):
        self.janelaPrincipal.title("Tela Principal")
        self.janelaPrincipal.geometry("1920x1080")
        self.janelaPrincipal.maxsize(1920, 1080)
        self.janelaPrincipal.minsize(1280, 720)
        self.janelaPrincipal.iconbitmap("icon.ico")

    def telaP():
        pass