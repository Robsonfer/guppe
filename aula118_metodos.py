"""
POO - MÉTODOS

Métodos (funções): Representam os comportamentos do objeto, ou seja, as ações que este objeto pode realizar no seu sistema.

Em Python dividimos os métodos em dois grupos: Métodos de Instância e Métodos de Classe.

MÉTODOS DE INSTÂNCIA

O método __init__ é um método especial chamado de construtor e sua função é construir o objeto a partir da classe.
Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline).
Os Métodos/Funções Dunder em Python são chamados de Métodos Mágicos.

ATENÇÃO: Por mais que possamos criar nossas próprias funções utilizando dunder, não é aconselhado.
    O Python possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento
    dessas funções mágicas internas da linguagem. Portanto nunca faça isso!

Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por underline.
"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:
    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """
        Retorna o valor do produto com desconto
        :param porcentagem:
        :return:
        """
        return (self.__valor * (100 - porcentagem)) / 100


# Importando biblioteca para criptografar as senhas da classe Usuario:

from passlib.hash import pbkdf2_sha256 as cryp


"""

# TIRE OS COMENTÁRIOS PARA FAZER A PARTE DE MÉTODOS DE INSTÂNCIA

# HAVERÁ A MESMA CLASSE REFATORADA PARA A PARTE DE MÉTODOS DE CLASSE!

class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

"""

######################### TRECHO DE CÓDIGOS USANDO MÉTODOS DE INSTÂNCIA #########################

"""
# Testando o método desconto:

produto1 = Produto('Playstation 5', 'Vídeo Game', 2300)

print(f'O valor do Pruduto com desconto é de R$ {produto1.desconto(20)}')

# Ou também podemos fazer assim, passando o self = produto1 e a porcentagem de desconto:
print(f'O valor do Pruduto com desconto é de R$ {Produto.desconto(produto1, 50)}')


# Testando o método nome_completo:

user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '654321')

print(user1.nome_completo())
print(user2.nome_completo())

"""


"""
Testando o acesso à senha:

print(f'Senha user1: {user1._Usuario__senha}') # Acesso de forma errada a um atributo de classe para mostrar uma insegurança
print(f'Senha user2: {user2._Usuario__senha}') # Acesso de forma errada a um atributo de classe para mostrar uma insegurança
# Note que mesmo fazendo acesso de forma errada, nós conseguimos obter a senha dos usuários

"""


"""

# Cadastro e verificação de usuário e senha usando Métodos de Instância

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere!')
    exit(1)

print('Usuário criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso Permitido')
else:
    print('Acesso Negado')

print(f'Senha User Criptografada: {user._Usuario__senha}') # OBS: Acesso errado!

"""


######################### TRECHO DE CÓDIGOS USANDO MÉTODOS DE CLASSE #########################

# Refatorando a Classe Usuario:


"""
class Usuario:

    contador = 0

    @classmethod # para uar métodos de classe deve-se usar antes este decorator
    def conta_usuarios(cls): # a partir do decorator, não usamos mais self, mas cls
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema.')
    
    @classmethod
    def ver(cls):
        print('Teste')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


# Testando a Classe Usuario:

user1 = Usuario('Robson', 'Ferreira', 'robsonnfer@gmail.com', '123456789')

Usuario.conta_usuarios() # forma correta

user1.conta_usuarios() # possível, mas incorreta

"""


"""
IMPORTANTE: Os Métodos de Classe são conhecidos como Métodos estáticos me outras linguagens.

Os métodos de instância são métodos que acessam atributos de instância.
Os métodos de classe são métodos que não acessam os atributos de instância, mas pode acessar atributos de classe.
"""


######################### TRECHO DE CÓDIGOS USANDO MÉTODOS PRIVADOS #########################


# Refatorando a Classe Usuario para mostrar o uso de Métodos Privados:

"""
class Usuario:

    contador = 0

    @classmethod # para uar métodos de classe deve-se usar antes este decorator
    def conta_usuarios(cls): # a partir do decorator, não usamos mais self, mas cls
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema.')
    
    @classmethod
    def ver(cls):
        print('Teste')

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    
    def __gera_usuario(self):
        return self.__email.split('@')[0]

user = Usuario('Robson', 'Ferreira', 'robsonnfer@gmail.com', '123456789')

# Ao tentar acessar o método privado desta forma abaixo temos um erro:
# print(user.__gera_usuario())

# AttributeError: 'Usuario' object has no attribute '__gera_usuario'

# Uma forma ruim e errada de fazer o acesso mas que funciona, seria assim:
print(user._Usuario__gera_usuario())

"""


######################### TRECHO DE CÓDIGOS USANDO MÉTODOS ESTÁTICOS #########################


class Usuario:

    contador = 0

    @classmethod # para uar métodos de classe deve-se usar antes este decorator
    def conta_usuarios(cls): # a partir do decorator, não usamos mais self, mas cls
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema.')
    
    @classmethod
    def ver(cls):
        print('Teste')
    
    # Criando nosso método estático:
    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'
    
    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False
    
    def __gera_usuario(self):
        return self.__email.split('@')[0]


"""
IMPORTANTE:

No método de instância, a gente tem acesso à instância do objeto;
No método de classe, não temos acesso à instância do objeto, somente à classe;
No método estático, não temos acesso nem à instância e nem à classe, note que não temos o 'cls' dentro dos parênteses do método!
"""

# Testando Método Estático:

print(Usuario.contador)
print(Usuario.definicao())

user = Usuario('Robson', 'Ferreira', 'robsonnfer@gmail.com', '123456789')

print(user.contador)
print(user.definicao())
