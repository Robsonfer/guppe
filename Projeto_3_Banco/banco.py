from typing import List
from time import sleep

from Projeto_3_Banco.models.cliente import Cliente
from Projeto_3_Banco.models.conta import Conta

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print('=====================================================================')
    print('=============================== ATM =================================')
    print('============================ Geek Bank ==============================')
    print('=====================================================================')
    print('|                  Selecione uma opção no menu:                     |')
    print('|                  1 - Criar conta                                  |')
    print('|                  2 - Efetuar saque                                |')
    print('|                  3 - Efetuar depósito                             |')
    print('|                  4 - Efetuar transferência                        |')
    print('|                  5 - Listar contas                                |')
    print('|                  6 - Sair do sistema                              |')
    print('=====================================================================')

    opcao: int = int(input('                   Informe sua opção: '))

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print('Foi um prazer servi-lo. Volte sempre!')
        sleep(3)
        exit(0)
    else:
        print('Atenção, opção inválida! Favor escolhe uma opção válida.')
        sleep(2)
        menu()


def criar_conta() -> None:
    print('Informe os dados do cliente: ')
    nome: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('CPF do cliente: ')
    data_nascimento: str = input('Data de nascimento do cliente: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print('Conta criada com sucesso!')
    print('Dados da conta: ')
    print('-----------------------------------------------------')
    print(conta)
    print('-----------------------------------------------------')
    sleep(5)
    print('\n')
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Por favor, informe o valor do saque: '))
            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta com número {numero}!')
    else:
        print('ATENÇÃO! Ainda não existem contas cadastradas!')
    sleep(3)
    print('\n')
    menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Por favor, informe o número da conta para depósito: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Por favor, informe o valor do depósito: '))
            conta.depositar(valor)
        else:
            print(f'Não foi encontrada a conta com número {numero}!')
    else:
        print('ATENÇÃO! Ainda não existem contas cadastradas!')
    sleep(3)
    print('\n')
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Por favor, informe o número da sua conta: '))

        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input("Por favor informe o número da conta destino: "))

            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input('Por favor, informe o valor da transferência: '))
                conta_o.transferir(conta_d, valor)
            else:
                print(f'A conta com número o {numero_d} não foi encontrada!')
        else:
            print(f'A sua conta com número o {numero_o} não foi encontrada!')
    else:
        print('ATENÇÃO! Ainda não existem contas cadastradas!')
    sleep(3)
    print('\n')
    menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print('-------------------------------------------------')
        print('--------------- Listagem de contas --------------')
        print('-------------------------------------------------')

        for conta in contas:
            print(conta)
            print('-------------------------------------------------')
        sleep(5)
        print('\n')
        menu()
    else:
        print('ATENÇÃO! Ainda não existem contas cadastradas!')
    sleep(3)
    print('\n')
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta

    return c


if __name__ == '__main__':
    main()
