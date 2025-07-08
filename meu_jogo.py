import random

numero_secreto = random.randint(1, 10)
tentativa = int(input("Adivinhe um número entre 1 e 10: "))

if tentativa == numero_secreto:
    print("Parabéns! Você acertou!")
else:
    print(f"Não foi dessa vez. O número era {numero_secreto}.")
