from Usuario import Usuario

class Cliente(Usuario):
    def __init__(self, nome, idade, cpf, nascimento, RG, bairro, cidade, estado, celular, estado_civil, profissao, nacionalidade):
        self.__estado_civil = estado_civil
        self.__profissao = profissao
        self.__nacionalidade = nacionalidade
        super().__init__(nome, idade, cpf, nascimento, RG, bairro, cidade, estado, celular)

    def getEstadoCivil(self):
        return self.__estado_civil

    def setEstadoCivil(self, estado_civil):
        self.__estado_civil = estado_civil

    def getProfissao(self):
        return self.__profissao

    def setProfissao(self, profissao):
        self.__profissao = profissao

    def getNacionalidade(self):
        return self.__nacionalidade 

    def setNacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade

