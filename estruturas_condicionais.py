# Definindo constantes para as idades de referência
MAIOR_IDADE = 18         # Idade mínima para tirar a CNH
IDADE_ESPECIAL = 17      # Idade permitida para iniciar aulas teóricas

# Solicitando a idade do usuário
idade = int(input("Informe sua idade: "))

# Verificação 1: usando dois 'if' separados (não recomendado, mas mostrado para fins didáticos)
print("\n[Verificação 1 - Dois 'if' separados]")
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

# Verificação 2: usando 'if' com 'else' (mais eficiente)
print("\n[Verificação 2 - 'if' com 'else']")
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
else:
    print("Ainda não pode tirar a CNH.")

# Verificação 3: usando 'if', 'elif' e 'else' (mais completa)
print("\n[Verificação 3 - 'if', 'elif' e 'else']")
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH.")
elif idade >= IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH.")
