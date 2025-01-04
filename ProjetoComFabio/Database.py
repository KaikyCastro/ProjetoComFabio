import sqlite3

conexao = sqlite3.connect("database.db")

cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    Cpf INTEGER NOT NULL PRIMARY KEY, 
    Nome TEXT NOT NULL, 
    Email TEXT NOT NULL, 
    Numero INT NOT NULL)
''')

print("Tabela criada com sucesso!")