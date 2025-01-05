from Tela import Login
import mysql.connector 

# Conexão com o banco de dados
conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='cadastro')

cursor = conexao.cursor()
cursor.execute('INSERT INTO pessoas (nomev, nascimento, sexo, altura, peso, nacionalidade) VALUES ("Fabio", "2004-01-20", "F", "1.50", "130.0", "Africano")');
conexao.commit()


cursor.close()
conexao.close()
tela = Login()