"""
Exercício 002

Peça o nome e a idade do usuário e exiba uma frase simples apresentando essas informações.
"""

# Seu código começa aqui

import os
os.system("cls")

nome = input("Digite seu Nome: ")
idade = int(input("Digite sua Idade: "))

print(f"Olá {nome}, você tem {idade} anos!")