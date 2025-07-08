# 🔢 Definindo duas variáveis com o mesmo valor
saldo = 1000
limite = 1000

# 🧠 Verificando se 'saldo' e 'limite' são o MESMO objeto na memória
print(saldo is limite)  # True — Python otimiza inteiros pequenos e aponta para o mesmo objeto

# ❗ Verificando se 'saldo' e 'limite' NÃO são o mesmo objeto
print(saldo is not limite)  # False — porque eles são o mesmo objeto
