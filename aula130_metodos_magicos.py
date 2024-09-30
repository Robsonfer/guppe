"""
POO - MÉTODOS MÁGICOS

Métodos Mágicos são todos os métodos que utilizam dunder.

dunder = Double Underscore

dunder init -> __init__() - Construtor de uma classe
dunder repr -> __repr__() - Representação do Objeto
"""
from aula030_dicionarios import outro


# Exemplos:


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # __str__()
    def __str__(self):
        return self.titulo

    # IMPORTANTE: __str__() tem preferência sobre __repr__()

    # __repr__()
    # Esse método sobrescreve a representação de nosso objeto e no lugar coloca o título
    def __repr__(self):
        return f'Livro {self.titulo} escrito por {self.autor}'

    def __len__(self):
        return self.paginas

    # __del__() Nesse caso, retorna um recado quando uma instância de um objeto é deletada:
    def __del__(self):
        print('Um objeto do tipo livro foi deletado da memória')

    # __add__() concatena dois objetos:
    def __add__(self, outro):
        return f'{self} - {outro}'

    # __mul__() multiplica o objeto:
    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Python Rocks', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

print(livro1)
print(livro2)

print(repr(livro1))
print(repr(livro2))

print(f'O livro {livro1.titulo} tem {len(livro1)} páginas')
print(f'O livro {livro2.titulo} tem {len(livro2)} páginas')

print(livro1 + livro2)

print(livro1 * 3)
