from Tela import Login
from Database import Database_cliente

cpf = "134.301.123-09"
nome = "Lais Mickaelly Pereira da Silva"
nascimento = "2004-05-30"
sexo = "F"
estado_civil = "Solteiro(a)"
telefone = "83998642050"
INCRA = "d1ds"
CAR = "d2s"

sgbd = Database_cliente()
sgbd.conectar()
sgbd.inserir_cliente_sem_Incra_CAR(cpf, nome, nascimento, sexo, estado_civil, telefone)
#sgbd.deletar_cliente(cpf)
#sgbd.inserir_cliente(cpf, nome, nascimento, sexo, estado_civil, telefone, INCRA, CAR)
#sgbd.pesquisar_cliente(cpf)
#sgbd.update_cliente(cpf, nome, nascimento, sexo, estado_civil, telefone, INCRA, CAR)
sgbd.desconectar()

#tela = Login()