"""
Exercício 011

Crie um programa que peça ao usuário as seguintes informações: nome, idade, cidade, curso, instituição e objetivo profissional. Ao final, exiba uma apresentação completa e bem organizada no terminal, usando várias linhas.
"""

# Seu código começa aqui

import os
os.system("cls")

nome = input("Digite seu Nome: ")
idade = int(input("Digite sua Idade: "))
cidade  = input("Digite a Cidade em que você mora: ")
curso = input("Digite o seu Curso: ")
instituicao = input("Digite a Instituição em que estuda: ")
objetivo = input("Digite seu Objetivo Profissional: ")

print(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[NOME].....................{nome}
[IDADE]....................{idade}
[CIDADE]...................{cidade}
[CURSO]....................{curso}
[INSTITUIÇÃO]..............{instituicao}
[OBJETIVO PROFISSIONAL]....{objetivo}
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")