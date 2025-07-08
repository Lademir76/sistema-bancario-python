# operadores_logicos.py

# 🧪 Exemplos básicos com operadores lógicos
print(True and True and True)        # True
print(True and False and True)       # False
print(False and False and False)     # False

print(True or True or True)          # True
print(True or False or False)        # True
print(False or False or False)       # False

# 💰 Cenário bancário
saldo = 1000
saque = 250
limite = 200
conta_especial = True

# 🧠 Expressão lógica sem parênteses
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)

# 🧠 Expressão lógica com parênteses para clareza
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)

# ✅ Verificações separadas
conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

print("Conta normal pode sacar?", conta_normal_com_saldo_suficiente)
print("Conta especial pode sacar?", conta_especial_com_saldo_suficiente)

