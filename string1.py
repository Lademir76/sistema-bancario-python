# Define uma string com letras maiúsculas e minúsculas misturadas
nome = "LAdEmIR"

# Exibe o nome todo em letras maiúsculas
print(nome.upper())

# Exibe o nome todo em letras minúsculas
print(nome.lower())

# Exibe o nome com a primeira letra de cada palavra em maiúscula
print(nome.title())

# Define uma string com espaços no início e no fim
texto = " Olá mundo! "

# Imprime a string original com um ponto no final
print(texto + ".")

# Remove espaços no início e no fim da string
print(texto.strip() + ".")

# Remove apenas os espaços à direita (final da string)
print(texto.rstrip() + ".")

# Remove apenas os espaços à esquerda (início da string)
print(texto.lstrip() + ".")

# Define uma string simples para representar um item de menu
menu = "Python"

# Adiciona decorações antes e depois da palavra
print("###" + menu + "###")

# Centraliza a palavra em um espaço de 14 caracteres (preenchido com espaços)
print(menu.center(14))

# Centraliza a palavra em 14 caracteres, preenchendo com o caractere "#"
print(menu.center(14, "#"))

# Insere um hífen entre cada letra da palavra
print("-".join(menu))
