"""
Aula 154 - Python Global Interpreter Lock

Aula teórica e prática

===============================================================================================
VER ARQUIVO 03-GIL-python-global-interpreter.pdf NESTE REPOSITÓRIO
===============================================================================================
A PRÁTICA DESTA AULA ESTÁ NOS ARQUIVOS single_thread.py | multi_thread.py | multi_processing.py
===============================================================================================

Tempo de processamento:

single_thread.py = 1.2797846794128418
multi_thread.py = 1.2721765041351318
multi_processing.py = 0.8257462978363037

Por causa do GIL, o processamento do programa single_thread.py e multi_thread.py não é muito diferente,
    entretanto a diferença entre estes dois e o multi_processing.py é considerável, mas é importante
    lembrar que o multi processing demanda mais recursos, portanto é mais pesado.
"""
