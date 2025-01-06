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
        self.inserirTab = f'INSERT INTO pessoas (nomev, nascimento, sexo, altura, peso, nacionalidade) VALUES ("{self.nomev}", "{self.nascimento}", "{self.sexo}", "{self.altura}","{self.peso}", "{self.nacionalidade}")'
        self.cursor.execute(self.inserirTab)

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