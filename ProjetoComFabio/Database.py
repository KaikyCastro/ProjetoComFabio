import mysql.connector
lista = []


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

    def inserir_cliente_sem_Incra_CAR(self, cpf, nome, nascimento, sexo, estado_civil, telefone):
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.telefone = telefone
     
        try:
            if self.cpf == '' or self.nome == '' or self.nascimento == '' or self.sexo == '' or self.estado_civil == ''  or self.telefone == '':
                print("Todos os campos sao obrigatorios")
            else:
                self.inserirTabCliente = f'INSERT INTO Cliente (cpf, nome, nascimento, sexo, estado_civil, telefone) VALUES ("{self.cpf}", "{self.nome}", "{self.nascimento}", "{self.sexo}", "{self.estado_civil}", "{self.telefone}")'
                self.cursor.execute(self.inserirTabCliente)
        except ValueError:
            print("Erro nos valores")

    def inserir_cliente(self, cpf, nome, nascimento, sexo, estado_civil, telefone, CAR, INCRA):
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.telefone = telefone
        self.CAR = CAR
        self.INCRA = INCRA

        try:
            if self.cpf == '' or self.nome == '' or self.nascimento == '' or self.sexo == '' or self.estado_civil == ''  or self.telefone == '':
                print("Todos os campos sao obrigatorios")
            else:
                self.inserirTabCliente = f'INSERT INTO Cliente (cpf, nome, nascimento, sexo, estado_civil, telefone, CAR, INCRA) VALUES ("{self.cpf}", "{self.nome}", "{self.nascimento}", "{self.sexo}", "{self.estado_civil}", "{self.telefone}", "{self.CAR}", "{self.INCRA}")'
                self.cursor.execute(self.inserirTabCliente)
        except ValueError:
            print("Erro nos valores")

    def pesquisar_cliente(self, cpf):
        self.cpf = cpf
        self.search = f'SELECT cpf FROM Cliente WHERE cpf = "{cpf}"'
        self.cursor.execute(self.search)
        self.resultado = self.cursor.fetchall()
        print(self.resultado)

        
        if (self.resultado == lista):
            print("Nao existe esse cpf cadastrado!")
        
      
    def deletar_cliente(self, cpf):
        self.cpf = cpf
        self.delet = f'DELETE FROM Cliente WHERE cpf = "{cpf}"'
        self.cursor.execute(self.delet)

    def update_cliente(self, cpf, nome, nascimento, sexo, estado_civil, telefone, CAR, INCRA):
        self.cpf = cpf
        self.nome = nome
        self.nascimento = nascimento
        self.sexo = sexo
        self.estado_civil = estado_civil
        self.telefone = telefone
        self.CAR = CAR
        self.INCRA = INCRA

        self.atualizar = f'UPDATE Cliente SET nome = "{self.nome}", nascimento = "{self.nascimento}", sexo = "{self.sexo}", estado_civil = "{self.estado_civil}", telefone = "{self.telefone}", CAR = "{self.CAR}", INCRA = "{self.INCRA}" WHERE cpf = "{self.cpf}"'
        self.atual = self.cursor.execute(self.atualizar)