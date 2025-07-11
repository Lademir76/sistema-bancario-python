import tkinter as tk
from tkinter import messagebox

def analisar_vogais():
    texto = entrada_texto.get()
    vogais = "AEIOUaeiou"
    encontradas = [letra for letra in texto if letra in vogais]

    resultado = f"Vogais encontradas: {', '.join(encontradas)}\nTotal: {len(encontradas)}"
    messagebox.showinfo("Resultado", resultado)

# Criando a janela principal
janela = tk.Tk()
janela.title("Analisador de Vogais")
janela.geometry("400x200")

# Widgets
label_instrucao = tk.Label(janela, text="Digite um texto abaixo:")
label_instrucao.pack(pady=10)

entrada_texto = tk.Entry(janela, width=50)
entrada_texto.pack(pady=5)

botao_analisar = tk.Button(janela, text="Analisar Vogais", command=analisar_vogais)
botao_analisar.pack(pady=20)

# Executando a interface
janela.mainloop()
