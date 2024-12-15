"""
Aula 175 - Alertas sobre sintaxes perigosas

Por exemplo:

É comum que os desenvolvedores confundam o uso entre '==' e 'is´:
    == -> usado para checar valores
    is -> usado para checar se os objetos são os mesmos.
"""

versao = '3.8'
print(versao is '3.8')

# Note que ele retorna o resultado do print, mas ainda assim traz consigo um SyntaxWarning
