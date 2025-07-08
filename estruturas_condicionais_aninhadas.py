# Define o tipo de conta: apenas uma deve ser True por vez
conta_normal = False
conta_universitaria = False
conta_especial = True

# Define o saldo atual da conta
saldo = 2000

# Define o valor que o cliente deseja sacar
saque = 1500

# Define o valor disponível no cheque especial (limite extra)
cheque_especial = 450

# Verifica se a conta é do tipo normal
if conta_normal:
    # Se o saldo for suficiente para o saque
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    # Se o saldo não for suficiente, mas o saldo + cheque especial cobrem o saque
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    # Se nem o saldo nem o cheque especial forem suficientes
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")

# Verifica se a conta é do tipo universitária
elif conta_universitaria:
    # Conta universitária não tem cheque especial, então só permite saque se houver saldo
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")

# Verifica se a conta é do tipo especial
elif conta_especial:
    # Apenas informa o tipo de conta; não há lógica de saque implementada aqui
    print("Conta especial selecionada!")

# Caso nenhum tipo de conta tenha sido selecionado
else:
    print("Entre em contato com seu gerente.")
