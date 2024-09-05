"""
POO - ATRIBUTOS

Atributos: Representam as características do objeto, ou seja, pelos atributos nós conseguimos representar
computacionalmente os estados de um objeto.

Em Python dividimos os atributos em três grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinâmicos.

ATRIBUTO DE INSTÂNCIA: São atributos declarados dentro do método construtor.

OBS: O Método Construtor é um método especial utilizado para a construção do objeto.


"""

print('-------------- ATRIBUTOS DE INSTÂNCIA --------------')


# Exemplo de Atributos de instância:

class Lampada:
    def __init__(self, voltagem, cor):
        self.__voltagem = voltagem
        self.__cor = cor
        self.__ligada = False


# Seguem as demais classes conforme aula anterior:
# As classes abaixo são Classes com Atributos de Instância Públicos

class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


"""
SOBRE A ESTRUTURA DO MÉTODO E SEUS ATRIBUTOS:

TRADUZINDO O MÉTODO ACIMA:
    1 - Logo na primeira linha declaramos a classe chamada Usuario
    2 - Em seguida criamos o método de inicialização onde nós declaramos como parâmetros:
        self (o próprio objeto);
        nome;
        email;
        senha;
    Com exceção do próprio objeto, todos estes parâmetros de instância são parâmetros comuns do objeto Usuario
    3 - Nas linhas abaixo onde está escrito self.nome = nome e demais leia-se:
        O objeto Usuario, no atributo nome vai receber nome;
        O objeto Usuario, no atributo email vai receber email;
        O objeto Usuario, no atributo senha vai receber senha.

O mesmo funciona para todas as demais classes. 

SIGNIFICADO DO SELF
O que significa o self declarado como primeiro parâmetro do método?
    Ele serve para informar que o próprio objeto é responsável pela execução do método.

Dica Geek: A palavra self na verdade é uma convenção, mas não é obrigação. Veja o exemplo abaixo. O método
    funcionará perfeitamente, ainda que o primeiro parâmetro seja definido como cerveja, mas veja que o Python
    vai te orientar a alterar o nome, pois não segue os padrôes da linguagem.
    Portanto, o primeiro parâmetro de um método é sempre self.
"""


class Teste:
    def __init__(cerveja, nome, idade):
        cerveja.nome = nome
        cerveja.idade = idade


"""
ATRIBUTOS PÚBLICOS E ATRIBUTOS PRIVADOS:

Em Python, por convenção, ficou estabelecido que todo atributo de uma classe é público. Ou seja, pode ser 
    acessado em todo o projeto.

Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser  
    acessado/utilizado somente dentro da própria classe onde está declarado, utiliza-se __ (duplo underline) no 
    início de seu nome.

Isso é conhecido também como Name Mangling.
"""


# Classes com Atributos de Instância Privados:

class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


"""
OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python não vai impedir que façamos 
    acesso aos atributos sinalizados fora da classe.
"""

# Exemplo:

user = Acesso('user@gmail.com', '123456')

print(user.email)
# Como mudamos o atributo email da classe Acesso para público, conseguimos imprimir este atributo fora da classe

# print(user.__senha)

"""
Neste caso recebemos um AttributeError, mas é só uma etapa de aviso. Desta forma não conseguimos acessar.
E se usaros o dir()? Veja a primeira informação que aparece. Basta imprimir user._Acesso__senha que teremos acesso.
Mas não deveríamos fazer este acesso! Utilizar somente em casos de testes ou em último caso.

O que podemos fazer é criar um outro método dentro da classe que imprime a senha, e depois chamar com 
    user.mostra_senha()
"""
print(dir(user))

print(user._Acesso__senha)  # Este é o Name Mangling (Confusão de Nomes)

# Imprimindo a senha (atributo privado) depois de criar um método dentro da classe:
user.mostra_senha()

# Imprimindo o email da mesma forma, mesmo sendo um atributo público:
user.mostra_email()

"""
Para fechar este tópico, o que significa Atributos de Instância?
    Significa que ao criarmos instâncias/objetos de uma classe, todas as instâncias terão estes atributos.
"""

# Exemplo

# Aqui temos duas instâncias/objetos da classe Acesso:
user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '654321')

print('Chamando o atributo email do objeto user1:')
user1.mostra_email()

print('Chamando o atributo email do objeto user2:')
user2.mostra_email()

print('-------------- ATRIBUTOS DE CLASSE --------------')

# Para explicar sobre atributos de classe usaremos a classe já construída Produto

# Nos atributos de instância cada objeto instanciado tem os seus próprios atributos:
p1 = Produto('Playtation 4', 'Vídeo Game', 2300)
p2 = Produto('Xbox S', 'Video Game', 4500)

"""
Os atributos de classe são aqueles declarados diretamente na classe, ou seja, fora do construtor. Geralmente já
    inicializamos um valor e este valor é compartilhado entre todas as instâncias da classe.
Ao invés de cada instância da classe ter seus próprios valores como é o caso dos atributos de instância, com os
    atributos de classe, todas as instâncias terão o mesmo valor para este atributo.
"""


# Exemplo:

class Product:

    # Atributo de classe
    tax = 1.05  # 5% de imposto
    counter = 0

    def __init__(self, name, description, value):
        self.id = Product.counter + 1
        self.name = name
        self.description = description
        self.value = (value * Product.tax)
        Product.counter = self.id


product1 = Product('Playstation 4', 'Sony Video Game Console', 2300)
product2 = Product('Xbox S', 'Microsoft Video Game Console', 4500)


print('---- Name ----')
print(f'Product1 name: {product1.name}')
print(f'Product2 name: {product2.name}')
print('---- Description ----')
print(f'Product1 description: {product1.description}')
print(f'Product2 description: {product2.description}')
print('---- Tax ----')
print(f'Product1 Tax value: {product1.tax}') # Acesso possível, mas incorreto. Abaixo acesso direto (correto)
print(f'Product2 Tax value: {product2.tax}') # Acesso possível, mas incorreto. Abaixo acesso direto (correto)
print('---- Final Value ----')
print(f'Product1 final value: {product1.value}')
print(f'Product2 final value: {product2.value}')

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe!

# Exemplo:

print(f'Acesso direto sem instanciar o atributo de classe: {Product.tax}')

# Implementando o atributo de classe id que atribui um nº de identificação automaticamente a cada objeto instanciado:
print(product1.id)
print(product2.id)

# OBS: Em linguagens como o Java, os atributos de classe são chamados de atributos estáticos!


print('-------------- ATRIBUTOS DE DINÂMICOS --------------')

"""
Um atributo dinâmico nada mais é que um atributo de instância que pode ser criado em tempo de execução.

OBS: O atributo dinâmico será exclusivo da instância que o criou.

Importante: Existe essa possibilidade de criar atributos dinâmicos, mas não é comum ser feito.
"""

# Exemplo usando a classe Product já criada anteriormente

# Criando um atributo dinâmico em tempo de execução:

product2.weight = '5kg' # Note que na classe Produto não existe o atributo peso

print(f'Product2 name: {product2.name}')
print(f'Product2 description: {product2.description}')
print(f'Product2 value: {product2.value}')
print(f'Product2 weight: {product2.weight}')

# Deletando atributos:

# Para deletar, vamos instanciar um novo objeto na classe produto:

product3 = Product('Super Nintendo', 'Nintendo 16 bits Video Game Console', 700)

# Vamos verificar o dict dos nossos produtos:
print(product1.__dict__)
print(product2.__dict__)
print(product3.__dict__)

# Vamos tentar fazer o mesmo com a nossa classe Product:
print(Product.__dict__)

# Deletando na instância product2 o atributo weight:
del product2.weight

# Verificando se o atributo peso foi deletado:
print(product2.__dict__)

# Deletando na instância product3 o atributo value:
del product3.value

# conferindo  se o atributo value foi deletado:
print(product3.__dict__)
