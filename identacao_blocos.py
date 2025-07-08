# 🔹 Função para realizar um saque

def sacar(valor):
    saldo = 500  # Define o saldo inicial

    # 🔸 Início de um bloco condicional
    if saldo >= valor:
        # Estas linhas estão indentadas com 4 espaços e pertencem ao bloco do 'if'
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    # Esta linha está fora do bloco 'if' e será executada sempre que a função for chamada
    print("Obrigado por ser nosso cliente, tenha um bom dia!")

# 🔹 Função para realizar um depósito
def depositar(valor):
    saldo = 500  # Define o saldo inicial
    saldo += valor  # Adiciona o valor ao saldo

# 🔸 Chamada da função sacar com o valor 1000
sacar(1000)
