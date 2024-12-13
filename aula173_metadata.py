"""
Aula 173 - Metadata
"""

from importlib import metadata

# Com esse recurso, podemos verificar a versão de qualquer pacote que nós temos, por exemplo:
print(metadata.version('pip'))

# Podemos ver quais são os metadados disponíveis em qualquer pacote. Por exemplo:
metadados_pip = metadata.metadata('pip')
print(list(metadados_pip))

# Como geramos em lista, podemos também fazer isso:
print(metadados_pip['Project-URL'])
print(metadados_pip['Author-email'])
# Mas se gerarmos sem o formato lista, nós teremos a informação completa.

# Vamos supor que precisamos saber quantos arquivos tem no pacote pip:
print(len(metadata.files('pip')))

# Ou podemos verificar, quais são os outros pacotes que este pacote pip requer:
print(metadata.requires('pip'))

# Ou no caso do django:
print(metadata.requires('django'))
