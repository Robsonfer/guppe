# Tipo String

# Em Python um dado é considerado do tipo string sempre que:

# Estiver entre aspas simples -> 'uma string', '234'
# Estiver entre aspas duplas -> "uma string", "234"
# Estiver entre aspas tripas simples -> '''uma string''', '''234'''
# Estiver entre aspas duplas triplas -> """uma string""", """234"""

nome = """Robson"""
print(nome)
print(type(nome))

nome = "Gina's Bar" # Como a string tem ' no meio tem que abrir aspas duplas para não dar erro
print(nome)
print(type(nome))

nome = 'Robson \nFerreira' # \n joga parte da string para a próxima linha
print(nome)
print(type(nome))

nome1 = 'Nome Idade Endereço'
print(nome1.split()) # Transforma em uma lista de strings
print(type(nome1))

nome2 = 'Geek University'
print(nome2[0:4])
print(len(nome))
