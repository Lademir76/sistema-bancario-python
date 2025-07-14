# Variáveis base
nome = "Lademir"
idade = 49
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

# Dicionário com dados
dados = {"nome": "Lademir", "idade": 49}

# 1. Formatação estilo antigo (%)
print("Nome: %s Idade: %d" % (nome, idade))  
# %s para string, %d para inteiro

# 2. Formatação com .format() - ordem padrão
print("Nome: {} Idade: {}".format(nome, idade))  

# 3. .format() com índices posicionais
print("Nome: {0} Idade: {1}".format(nome, idade))  

# 4. .format() com índices invertidos
print("Nome: {1} Idade: {0}".format(idade, nome))  

# 5. .format() com nomes de variáveis
print("{nome} tem {idade} anos".format(nome=nome, idade=idade))  

# 6. .format() com nomes diferentes dos das variáveis
print("{name} tem {age} anos".format(age=idade, name=nome))  

# 7. .format() com desempacotamento de dicionário
print("{nome} tem {idade}".format(**dados))  

# 8. f-string simples
print(f"Nome: {nome} Idade: {idade}")  

# 9. f-string com formatação de float (2 casas decimais)
print(f"Nome: {nome} Idade: {idade} Saldo:{saldo:.2f}")  

# 10. f-string com alinhamento à esquerda (10 caracteres)
print(f"Nome:{nome:<10}Idade:{idade:<10d}")  
# <10 alinha à esquerda ocupando 10 espaços































