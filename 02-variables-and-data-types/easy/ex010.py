"""
Exercício 010

Peça dois números ao usuário e exiba a soma entre eles.
"""

# Seu código começa aqui

from os import system 
system("cls")


n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
print(f"{n1} + {n2} = {n1+n2}")