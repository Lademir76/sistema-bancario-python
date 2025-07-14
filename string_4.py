# Define a variável com o nome
nome = "Lademir"

# Cria uma mensagem multilinha usando f-string
mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo Python.
Essa mensagem tem diferentes recuos.
"""
# A f-string permite inserir a variável 'nome' diretamente no texto

# Exibe a mensagem formatada
print(mensagem)

# Exibe um menu formatado com múltiplas linhas
print("""
================ MENU ================
1 - Depositar
2 - Sacar
0 - Sair
======================================
Obrigado por usar nosso sistema!!!!
""")
# Esse bloco usa aspas triplas para criar um texto multilinha, ideal para menus
