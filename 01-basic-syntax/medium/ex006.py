"""
Exercício 006

Peça ao usuário seu nome, idade, cidade e profissão. Depois, exiba uma apresentação simples reunindo todas essas informações em uma única saída organizada.
"""

# Seu código começa aqui

nome = input("Digite seu Nome: ")
idade = int(input("Digite sua Idade: "))
cidade = input("Digite a Cidade em que você mora: ")
profissao = input("Digite sua profissão: ")

print(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[NOME]........{nome}
[IDADE].......{idade}
[CIDADE]......{cidade}
[PROFISSÃO]...{profissao}
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")