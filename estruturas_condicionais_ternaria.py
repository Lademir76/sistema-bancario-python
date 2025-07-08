# Define o saldo disponível na conta
saldo = 3500

# Define o valor que se deseja sacar
saque = 2500

# Usa uma estrutura condicional ternária para definir o status da operação
# Se o saldo for suficiente para o saque, o status será "Sucesso", senão será "Falha"
status = "Sucesso" if saldo >= saque else "Falha"

# Exibe o resultado da tentativa de saque
print(f"{status} ao realizar o saque!")
