from Tela import Login
from Database import Database

ids = '2'
nomev = "pedro"
nascimento = "2005-03-14"
sexo = 'F'
altura = '1.40'
peso = '55'
nacionalidade = ''

sgbd = Database()
sgbd.conectar()
sgbd.inserir(nomev, nascimento, sexo, altura, peso, nacionalidade)
sgbd.desconectar()
tela = Login()