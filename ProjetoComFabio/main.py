from Tela import Login


# Conex�o com o banco de dados
conexao = connector.connect(
    host='localhost',
    user='root',
    password='',
    database='cadastro')

cursor = conexao.cursor()

cursor.close()
conexao.close()
tela = Login()