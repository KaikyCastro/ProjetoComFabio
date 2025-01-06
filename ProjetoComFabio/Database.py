import mysql.connector 

class Database():
    def __init__(self):
        pass

    def conectar(self):
        self.conexao = mysql.connector.connect(
                                          host='localhost',
                                          user='root',
                                          password='',
                                          database='cadastro')
        self.cursor = self.conexao.cursor()

    def desconectar(self):
        self.conexao.close()
        self.cursor.close()

    def inserir(self, nomev, nascimento, sexo, altura, peso, nacionalidade):
        self.nomev = nomev
        self.nascimento = nascimento
        self.sexo = sexo
        self.altura = altura
        self.peso = peso
        self.nacionalidade = nacionalidade
        self.inserirTab = f'INSERT INTO pessoas (nomev, nascimento, sexo, altura, peso, nacionalidade) VALUES ("{self.nomev}", "{self.nascimento}", 
        "{self.sexo}", "{self.alutra}","{self.peso}", "{self.nacionalidade}")'
        self.cursor.execute(self.inserirTab)
        self.cursor.commit()
