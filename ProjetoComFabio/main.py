from Tela import Login


# Conexão com o banco de dados
conexao = connector.connect(
    host='localhost',
    user='root',
    password='',
    database='cadastro')

cursor = conexao.cursor()

cursor.close()
conexao.close()
tela = Login()