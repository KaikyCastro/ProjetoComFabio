import mysql.connector
from Cpf import CPF
lista = []

class Database_colaborador():
    def __init__(self):
        pass

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                                              host='localhost',
                                              user='root',
                                              password='',
                                              database='Propriedade_Produtiva')
            self.cursor = self.conexao.cursor()
        except mysql.connector.DatabaseError:
            print("Nao foi possivel conectar ao banco dados")

    def desconectar(self):
        try:
            self.conexao.close()
            self.cursor.close()
        except mysql.connector.DatabaseError:
            print("Nao foi possivel desconectar o banco de dados")

    def inserir_colaborador(self, cpf, cargo, nome, telefone, senha):
        self.cpf = cpf
        self.cargo = cargo
        self.nome = nome
        self.telefone = telefone
        self.senha = senha
        self.testecpf = CPF(self.cpf)

        self.conectar()
        try:
            if self.testecpf.validate(self.cpf) == False:
                print("CPF invalido")
            elif self.cpf == '' or self.cargo == '' or self.nome == '' or self.telefone == '' or self.senha == '':
                print("Todos os campos sao obrigatorios")
            else:
                self.inserirTabColaborador = f'INSERT INTO Colaborador (cpf, cargo, nome, telefone, senha) VALUES ("{self.cpf}", "{self.cargo}", "{self.nome}", "{self.telefone}", "{self.senha}")'
                self.cursor.execute(self.inserirTabColaborador)
                self.desconectar()
        except ValueError:
            print("Erro nos valores")
            self.desconectar()

    def pesquisar_colaborador(self, cpf):
        self.cpf = cpf

        self.conectar()
        self.search = f'SELECT cpf FROM Colaborador WHERE cpf = "{cpf}"'
        self.cursor.execute(self.search)
        self.resultado = self.cursor.fetchall()
        print(self.resultado)
        if (self.resultado == lista):
            print("Nao existe esse cpf cadastrado!")
            
        self.desconectar()

    def deletar_colaborador(self, cpf):
        self.cpf = cpf

        self.conectar()
        self.delet = f'DELETE FROM Colaborador WHERE cpf = "{cpf}"'
        self.cursor.execute(self.delet)
        self.desconectar()

    def update_colaborador(self, cpf, cargo, nome, telefone, senha):
        self.cpf = cpf
        self.cargo = cargo
        self.nome = nome
        self.telefone = telefone
        self.senha = senha

        self.conectar()
        self.atualizar = f'UPDATE Colaborador SET cargo = "{self.cargo}", nome = "{self.nome}", telefone = "{self.telefone}", senha = "{self.senha}" WHERE cpf = "{self.cpf}"'
        self.atual = self.cursor.execute(self.atualizar)
        self.desconectar()



class Database_cliente():
    def __init__(self):
        pass

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                                              host='localhost',
                                              user='root',
                                              password='',
                                              database='Propriedade_Produtiva')
            self.cursor = self.conexao.cursor()
        except mysql.connector.DatabaseError:
            print("Nao foi possivel conectar ao banco dados")

    def desconectar(self):
        try:
            self.conexao.close()
            self.cursor.close()
        except mysql.connector.DatabaseError:
            print("Nao foi possivel desconectar o banco de dados")

    def inserir_cliente(self, cpf, nome, nascimento, sexo, estado_civil, telefone):
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.telefone = telefone
        self.testecpf = CPF(self.cpf)
     
        self.conectar()
        try:
            if self.testecpf.validate(self.cpf) == False:
                print("CPF invalido")
            elif self.cpf == '' or self.nome == '' or self.nascimento == '' or self.sexo == '' or self.estado_civil == ''  or self.telefone == '':
                print("Todos os campos sao obrigatorios")
            else:
                self.inserirTabCliente = f'INSERT INTO Cliente (cpf, nome, nascimento, sexo, estado_civil, telefone) VALUES ("{self.cpf}", "{self.nome}", "{self.nascimento}", "{self.sexo}", "{self.estado_civil}", "{self.telefone}")'
                self.cursor.execute(self.inserirTabCliente)
                self.desconectar()

        except ValueError:
            print("Erro nos valores")

    def pesquisar_cliente(self, cpf):
        self.cpf = cpf

        self.conectar()
        self.search = f'SELECT cpf FROM Cliente WHERE cpf = "{cpf}"'
        self.cursor.execute(self.search)
        self.resultado = self.cursor.fetchall()
        print(self.resultado)

        if (self.resultado == lista):
            print("Nao existe esse cpf cadastrado!")
            
        self.desconectar()
      
    def deletar_cliente(self, cpf):
        self.cpf = cpf

        self.conectar()
        self.delet = f'DELETE FROM Cliente WHERE cpf = "{cpf}"'
        self.cursor.execute(self.delet)
        self.desconectar()

    def update_cliente(self, cpf, nome, nascimento, sexo, estado_civil, telefone, CAR, INCRA):
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.telefone = telefone
        self.CAR = CAR
        self.INCRA = INCRA

        self.conectar()
        self.atualizar = f'UPDATE Cliente SET nome = "{self.nome}", nascimento = "{self.nascimento}", sexo = "{self.sexo}", estado_civil = "{self.estado_civil}", telefone = "{self.telefone}", CAR = "{self.CAR}", INCRA = "{self.INCRA}" WHERE cpf = "{self.cpf}"'
        self.atual = self.cursor.execute(self.atualizar)
        self.desconectar()


class Database_propriedade(Database_cliente):
    def __init__(self):
        pass

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                                              host='localhost',
                                              user='root',
                                              password='',
                                              database='Propriedade_Produtiva')
            self.cursor = self.conexao.cursor()
        except mysql.connector.DatabaseError:
            print("Nao foi possivel conectar ao banco dados")

    def desconectar(self):
        try:
            self.conexao.close()
            self.cursor.close()
        except mysql.connector.DatabaseError:
            print("Nao foi possivel desconectar o banco de dados")

    def inserir_propriedade(self, endereco, nome_da_propriedade):
        self.endereco = endereco
        self.nome_da_propriedade = nome_da_propriedade
        self.cpf_cliente = self.cpf

        self.conectar()
        try:
            if self.endereco == '' or self.nome_da_propriedade == '':
                print("Todos os campos sao obrigatorios")
            else:
                self.inserirTabPropriedade = f'INSERT INTO Propriedade (endereco, nome_da_propriedade, cpf_cliente) VALUES ("{self.endereco}", "{self.nome_da_propriedade}", "{self.cpf_cliente}")'
                self.cursor.execute(self.inserirTabPropriedade)
                self.desconectar()
        except ValueError:
            print("Erro nos valores")
            self.desconectar()

    def inserir_propriedade_car_incra(self, endereco, nome_da_proprieddade, CAR, INCRA):
        self.endereco = endereco
        self.nome_da_propriedade = nome_da_proprieddade
        self.CAR = CAR
        self.INCRA = INCRA

        self.conectar()
        try:
            if self.endereco == '' or self.nome_da_propriedade == '' or self.CAR == '' or self.INCRA == '':
                print("Todos os campos sao obrigatorios")
            else:
                self.inserirTabPropriedade = f'INSERT INTO Propriedade (endereco, nome_da_propriedade, CAR, INCRA) VALUES ("{self.endereco}", "{self.nome_da_propriedade}", "{self.CAR}", "{self.INCRA}")'
                self.cursor.execute(self.inserirTabPropriedade)
                self.desconectar()
        except ValueError:
            print("Erro nos valores")
            self.desconectar()

    def pesquisar_propriedade(self, endereco):
        self.endereco = endereco
        self.conectar()
        self.search = f'SELECT endereco FROM Propriedade WHERE endereco = "{endereco}"'
        self.cursor.execute(self.search)
        self.resultado = self.cursor.fetchall()
        print(self.resultado)
        if (self.resultado == lista):
            print("Nao existe esse endereco cadastrado!")
            
        self.desconectar()

    def deletar_propriedade(self, endereco):
        self.endereco = endereco

        self.conectar()
        self.delet = f'DELETE FROM Propriedade WHERE endereco = "{endereco}"'
        self.cursor.execute(self.delet)
        self.desconectar()

    def update_propriedade(self, endereco, nome_da_propriedade):
        self.endereco = endereco
        self.nome_da_propriedade = nome_da_propriedade

        self.conectar()
        self.atualizar = f'UPDATE Propriedade SET nome_da_propriedade = "{self.nome_da_propriedade}" WHERE endereco = "{self.endereco}"'
        self.atual = self.cursor.execute(self.atualizar)
        self.desconectar()

    def update_propriedade_car_incra(self, endereco, nome_da_propriedade, CAR, INCRA):
        self.endereco = endereco
        self.nome_da_propriedade = nome_da_propriedade
        self.CAR = CAR
        self.INCRA = INCRA

        self.conectar()
        self.atualizar = f'UPDATE Propriedade SET nome_da_propriedade = "{self.nome_da_propriedade}", CAR = "{self.CAR}", INCRA = "{self.INCRA}" WHERE endereco = "{self.endereco}"'
        self.atual = self.cursor.execute(self.atualizar)
        self.desconectar()