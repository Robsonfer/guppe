from Projeto_3_Banco.models.cliente import Cliente
from Projeto_3_Banco.models.conta import Conta

felicity = Cliente('Felicity Jones', 'felicity@gmail.com', '123.456.789-90', '02/09/1987')
angelina = Cliente('Angelina Jolie', 'angelina@gmail.com', '987.654.321-12', '08/07/1978')

# print(felicity)
# print(angelina)

contaf: Conta = Conta(felicity)
contaa: Conta = Conta(angelina)

# print(contaf)
# print(contaa)
