import tkinter as tk
from tkinter import ttk
import requests

def converter():
    try:
        valor = float(entry_valor.get())
    except ValueError:
        label_resultado.config(text="Digite um valor numérico válido.")
        return

    de_moeda = combo_de.get()
    para_moeda = combo_para.get()

    if not de_moeda or not para_moeda:
        label_resultado.config(text="Selecione as moedas.")
        return

    url = f"https://api.frankfurter.app/latest?amount={valor}&from={de_moeda}&to={para_moeda}"

    try:
        resposta = requests.get(url)
        dados = resposta.json()
        resultado = dados['rates'][para_moeda]
        label_resultado.config(text=f"{valor:.2f} {de_moeda} = {resultado:.2f} {para_moeda}")
    except Exception as e:
        label_resultado.config(text="Erro na conversão.")
        print("Erro:", e)
   

# Janela principal
janela = tk.Tk()
janela.title("Conversor de Moedas")

# Campo de valor
tk.Label(janela, text="Valor:").grid(row=0, column=0)
entry_valor = tk.Entry(janela)
entry_valor.grid(row=0, column=1)

# Seleção de moeda origem
tk.Label(janela, text="De:").grid(row=1, column=0)
combo_de = ttk.Combobox(janela, values=["USD", "BRL", "EUR", "JPY", "GBP"])
combo_de.grid(row=1, column=1)
combo_de.set("USD")

# Seleção de moeda destino
tk.Label(janela, text="Para:").grid(row=2, column=0)
combo_para = ttk.Combobox(janela, values=["USD", "BRL", "EUR", "JPY", "GBP"])
combo_para.grid(row=2, column=1)
combo_para.set("BRL")

# Botão de conversão
botao_converter = tk.Button(janela, text="Converter", command=converter)
botao_converter.grid(row=3, column=0, columnspan=2)

# Resultado
label_resultado = tk.Label(janela, text="")
label_resultado.grid(row=4, column=0, columnspan=2)

janela.mainloop()

