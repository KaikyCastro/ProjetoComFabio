import mysql.connector

class Database():
    def __init__(self):
        pass

    def conectar(self):
        try:
            self.conexao = mysql.connector.connect(
                                              host='localhost',
                                              user='root',
                                              password='',
                                              database='cadastro')
            self.cursor = self.conexao.cursor()
        except mysql.connector.DatabaseError:
            print("Nao foi possivel conectar ao banco dados")

    def desconectar(self):
        try:
            self.conexao.close()
            self.cursor.close()
        except mysql.connector.DatabaseError:
            print("Nao foi possivel desconectar o banco de dados")

    def inserir(self, nomev, nascimento, sexo, altura, peso, nacionalidade):
        self.nomev = nomev
        self.nascimento = nascimento
        self.sexo = sexo
        self.altura = altura
        self.peso = peso
        self.nacionalidade = nacionalidade

        try:
            if self.nomev == '' or self.nascimento == '' or self.sexo == '' or self.altura == '' or peso == '' or nacionalidade == '':
                print("Todos os campos sao obrigatorios")
            else:
                self.inserirTab = f'INSERT INTO pessoas (nomev, nascimento, sexo, altura, peso, nacionalidade) VALUES ("{self.nomev}", "{self.nascimento}", "{self.sexo}", "{self.altura}","{self.peso}", "{self.nacionalidade}")'
                self.cursor.execute(self.inserirTab)
        except ValueError:
            print("Valores addwdas")

    def pesquisar(self, ids):
        self.id = ids

        self.search = f'SELECT id FROM pessoas WHERE id = "{ids}"'
        self.cursor.execute(self.search)
        self.resultado = self.cursor.fetchall()
        print(self.resultado)
      
    def deletar(self, ids):
        self.ids = ids
        self.delet = f'DELETE FROM pessoas WHERE id = "{ids}"'
        self.cursor.execute(self.delet)

    def update(self, ids, nomev, nascimento, sexo, altura, peso, nacionalidade):
        self.ids = ids
        self.nomev = nomev
        self.nascimento = nascimento
        self.sexo = sexo
        self.altura = altura
        self.peso = peso
        self.nacionalidade = nacionalidade

        self.atualizar = f'UPDATE pessoas set nomev = "{self.nomev}", nascimento = "{self.nascimento}", sexo = "{self.sexo}", altura = "{self.altura}", peso = "{self.peso}", nacionalidade = "{self.nacionalidade} "WHERE id = {self.ids}'
        self.atual = self.cursor.execute(self.atualizar)