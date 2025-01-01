from Cpf import CPF

class Usuario(CPF):
    def __init__(self, nome, idade, cpf, nascimento, RG, bairro, cidade, estado, celular):
        self.__nome = nome
        self.__idade = idade
        self.__nascimento = nascimento
        self.__RG = RG
        self.__bairro = bairro
        self.__cidade = cidade
        self.__estado = estado
        self.__celular = celular
        super().__init__(cpf)

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getIdade(self):
        return self.__idade

    def setIdade(self, idade):
        self.__idade = idade

    def getNascimento(self):
        return self.__nascimento

    def setNascimento(self, nascimento):
        self.__nascimento = nascimento

    def getRG(self):
        return self.__RG

    def setRG(self, RG):
        self.__RG = RG  

    def getBairro(self):
        return self.__bairro

    def setBairro(self, bairro):
        self.__bairro = bairro

    def getCidade(self):
        return self.__cidade

    def setCidade(self, cidade):
        self.__cidade = cidade

    def getEstado(self):
        return self.__estado

    def setEstado(self, estado):
        self.__estado = estado

    def getCelular(self):
        return self.__celular

    def setCelular(self, celular):
        self.__celular = celular

    def validarCPF(self, cpf):
        return super().validate(cpf)


    def __str__(self):
        return f'Nome: {self.__nome}, Idade: {self.__idade}, CPF: {self.getCPF()}, Nascimento: {self.__nascimento}, RG: {self.__RG}, Bairro: {self.__bairro}, Cidade: {self.__cidade}, Estado: {self.__estado}, Celular: {self.__celular}'