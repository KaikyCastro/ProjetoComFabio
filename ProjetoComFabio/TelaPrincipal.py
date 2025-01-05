from Login import *

janelaPrincipal = ctk.CTkToplevel(master=janelaLogin, fg_color="white")

class TelaPrincipal(Login):
    def __init__(self):
        super().__init__()
        self.janelaPrincipal = janelaPrincipal
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