from Tela import Login
from Database import Database_cliente, Database_colaborador, Database_propriedade

cpf = "134.121.123-09"
nome = "Lais Mickaelly Pereira da Silva"
nascimento = "2004-05-30"
sexo = "F"
estado_civil = "Solteiro(a)"
telefone = "83998642050"
INCRA = "d1ds"
CAR = "d2s"
endereco = "Taquara"
nome_da_propriedade = "Fazenda do Taquara"

'''sgbd_cliente = Database_cliente()
sgbd_cliente.inserir_cliente_sem_Incra_CAR(cpf, nome, nascimento, sexo, estado_civil, telefone)
sgbd_cliente.deletar_cliente(cpf)
sgbd_cliente.inserir_cliente(cpf, nome, nascimento, sexo, estado_civil, telefone, INCRA, CAR)
sgbd_cliente.pesquisar_cliente(cpf)
sgbd_cliente.update_cliente(cpf, nome, nascimento, sexo, estado_civil, telefone, INCRA, CAR)'''

prop = Database_propriedade()
prop.inserir_propriedade(endereco, nome_da_propriedade)
#tela = Login()