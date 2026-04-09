"""
Exercício 009

Peça ao usuário informações para montar um pequeno cartaz de evento: nome do evento, data, horário, local e nome do organizador. Depois, exiba essas informações em um formato visualmente organizado no terminal, como se fosse um anúncio.
"""

# Seu código começa aqui

import os
os.system("cls")

print("Sobre o Evento informe:")
nome = input("Digite o Nome: ")
data = input("Digite a Data: ")
horario = input("Digite o Horário: ")
local = input("Digite o Local: ")
organizador = input("Digite o Nome do Organizador: ")

print(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[NOME]...........{nome}
[DATA]...........{data}
[HORÁRIO]........{horario}
[LOCAL]..........{local}
[ORGANIZADOR]....{organizador}
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")