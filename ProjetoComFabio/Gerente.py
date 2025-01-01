from Usuario import Usuario

class Gerente(Usuario):
    def __init__(self, nome, idade, cpf, nascimento, RG, bairro, cidade, estado, celular, salario, cargo, setor):
        self.__salario = salario
        self.__cargo = cargo
        self.__setor = setor
        super().__init__(nome, idade, cpf, nascimento, RG, bairro, cidade, estado, celular)
    def getSalario(self):
        return self.__salario

    def setSalario(self, salario):
        self.__salario = salario

    def getCargo(self):
        return self.__cargo
    def setCargo(self, cargo):
        self.__cargo = cargo

    def getSetor(self):
        return self.__setor

    def setSetor(self, setor):
        self.__setor = setor

    def __str__(self):
        return f"Nome: {self.getNome()}\nIdade: {self.getIdade()}\nCPF: {self.getCPF()}\nNascimento: {self.getNascimento()}\nRG: {self.getRG()}\nBairro: {self.getBairro()}\nCidade: {self.getCidade()}\nEstado: {self.getEstado()}\nCelular: {self.getCelular()}\nSalario: {self.getSalario()}\nCargo: {self.getCargo()}\nSetor: {self.getSetor()}"