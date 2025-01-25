import mysql.connector
from cpf import CPF
lista = []

class Database_colaborador():
    def __init__(self, cpf, cargo, nome, telefone, senha):
        self.cpf = cpf
        self.cargo = cargo
        self.nome = nome
        self.telefone = telefone
        self.senha = senha

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

    def inserir_colaborador(self):
        
        self.testecpf = CPF(self.cpf)

        self.conectar()
        
        if self.testecpf.validate(self.cpf) == False:
            print("CPF invalido")
        elif self.cpf == '' or self.cargo == '' or self.nome == '' or self.telefone == '' or self.senha == '':
            print("Todos os campos sao obrigatorios")
        else:
            self.inserirTabColaborador = f'INSERT INTO Colaborador (cpf, cargo, nome, telefone, senha) VALUES ("{self.cpf}", "{self.cargo}", "{self.nome}", "{self.telefone}", "{self.senha}")'
            self.cursor.execute(self.inserirTabColaborador)
            self.desconectar()
        

    def pesquisar_colaborador(self):
        self.conectar()
        self.search = f'SELECT * FROM Colaborador WHERE cpf = "{self.cpf}"'
        self.cursor.execute(self.search)
        self.resultado = self.cursor.fetchall()
        print(self.resultado)
        if (self.resultado == lista):
            print("Nao existe esse cpf cadastrado!")
            
        self.desconectar()

    def deletar_colaborador(self):
        self.conectar()
        self.delet = f'DELETE FROM Colaborador WHERE cpf = "{self.cpf}"'
        self.cursor.execute(self.delet)
        self.desconectar()

    def update_colaborador(self, cargo, nome, telefone, senha):
        self.conectar()
        self.atualizar = f'UPDATE Colaborador SET cargo = "{cargo}", nome = "{nome}", telefone = "{telefone}", senha = "{senha}" WHERE cpf = "{self.cpf}"'
        self.atual = self.cursor.execute(self.atualizar)
        self.desconectar()



class Database_cliente():
    def __init__(self, cpf, nome, nascimento, sexo, estado_civil, telefone):
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.telefone = telefone
        

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

    def inserir_cliente(self):
        self.testecpf = CPF(self.cpf)
     
        self.conectar()
        if self.testecpf.validate(self.cpf) == False:
            print("CPF invalido")
        elif self.cpf == '' or self.nome == '' or self.nascimento == '' or self.sexo == '' or self.estado_civil == ''  or self.telefone == '':
            print("Todos os campos sao obrigatorios")
        else:
            inserirTabCliente = f'INSERT INTO Cliente (cpf, nome, nascimento, sexo, estado_civil, telefone) VALUES ("{self.cpf}", "{self.nome}", "{self.nascimento}", "{self.sexo}", "{self.estado_civil}", "{self.telefone}")'
            self.cursor.execute(inserirTabCliente)
            self.desconectar()

    def pesquisar_cliente(self):
        self.conectar()
        self.search = f'SELECT * FROM Cliente WHERE cpf = "{self.cpf}"'
        self.cursor.execute(self.search)
        self.resultado = self.cursor.fetchall()
        print(self.resultado)

        if (self.resultado == lista):
            print("Nao existe esse cpf cadastrado!")
            
        self.desconectar()
      
    def deletar_cliente(self):
        self.conectar()
        self.delet = f'DELETE FROM Cliente WHERE cpf = "{self.cpf}"'
        self.cursor.execute(self.delet)
        self.desconectar()

    def update_cliente(self, nome, nascimento, sexo, estado_civil, telefone):
        self.conectar()
        self.atualizar = f'UPDATE Cliente SET nome = "{nome}", nascimento = "{nascimento}", sexo = "{sexo}", estado_civil = "{estado_civil}", telefone = "{telefone}" WHERE cpf = "{self.cpf}"'
        self.atual = self.cursor.execute(self.atualizar)
        self.desconectar()


class Database_propriedade():
    def __init__(self, endereco, nome_da_propriedade):
        self.endereco = endereco
        self.nome_da_propriedade = nome_da_propriedade
        self.CAR = ''
        self.INCRA = ''

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

    def inserir_propriedade(self):

        self.conectar()

        if self.endereco == '' or self.nome_da_propriedade == '':
            print("Todos os campos sao obrigatorios")
        else:
            self.inserirTabPropriedade = f'INSERT INTO Propriedade (endereco, nome_da_propriedade) VALUES ("{self.endereco}", "{self.nome_da_propriedade}")'
            self.cursor.execute(self.inserirTabPropriedade)
            self.desconectar()

        self.desconectar()

    def inserir_propriedade_car_incra(self, CAR, INCRA):
        self.CAR = CAR
        self.INCRA = INCRA

        self.conectar()
        if self.endereco == '' or self.nome_da_propriedade == '' or self.CAR == '' or self.INCRA == '':
            print("Todos os campos sao obrigatorios")
        else:
            self.inserirTabPropriedade = f'UPDATE Propriedade SET CAR = "{self.CAR}", INCRA = "{self.INCRA}" WHERE endereco = "{self.endereco}"'
            self.cursor.execute(self.inserirTabPropriedade)
            self.desconectar()
   
        self.desconectar()

    def pesquisar_propriedade(self):
        self.conectar()
        self.search = f'SELECT * FROM Propriedade WHERE endereco = "{self.endereco}"'
        self.cursor.execute(self.search)
        self.resultado = self.cursor.fetchall()
        print(self.resultado)
        if (self.resultado == lista):
            print("Nao existe esse endereco cadastrado!")
            self.desconectar()
            
        self.desconectar()

    def deletar_propriedade(self):
        self.conectar()
        self.delet = f'DELETE FROM Propriedade WHERE endereco = "{self.endereco}"'
        self.cursor.execute(self.delet)
        self.desconectar()

    def update_propriedade(self, nome_da_propriedade):
        self.conectar()
        self.atualizar = f'UPDATE Propriedade SET nome_da_propriedade = "{nome_da_propriedade}" WHERE endereco = "{self.endereco}"'
        self.atual = self.cursor.execute(self.atualizar)
        self.desconectar()

    def update_propriedade_car_incra(self, CAR, INCRA):
        self.conectar()
        self.atualizar = f'UPDATE Propriedade SET CAR = "{CAR}", INCRA = "{INCRA}" WHERE endereco = "{self.endereco}"'
        self.atual = self.cursor.execute(self.atualizar)
        self.desconectar()
