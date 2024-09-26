"""
POO - MÉTODOS MÁGICOS

Métodos Mágicos são todos os métodos que utilizam dunder.

dunder = Double Underscore

dunder init -> __init__()


"""


# Exemplos:


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # __repr__()
    # Esse método sobrescreve a representação de nosso objeto e no lugar coloca o título
    def __repr__(self):
        return f'Livro {self.titulo} escrito por {self.autor}'

    # __str__()
    def __str__(self):
        return self.titulo
    # IMPORTANTE: __str__() tem preferência sobre __repr__()

    def __len__(self):
        return self.paginas


livro1 = Livro('Python Rocks', 'Geek University', 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

print(livro1)
print(livro2)
print(len(livro1))
print(len(livro2))
