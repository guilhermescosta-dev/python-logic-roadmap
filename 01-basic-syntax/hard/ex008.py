"""
Exercício 008

Peça ao usuário seu nome, horário em que costuma estudar, matéria favorita, tempo médio diário de estudo e principal meta atual. Depois, exiba essas informações em formato de perfil de rotina, com cada item bem identificado.
"""

# Seu código começa aqui

nome = input("Digite seu Nome: ")
horario = input("Digite o horário/periodo que costuma estudar: ")
materia = input("Digite sua matéria favorita: ")
tmde = input("Digite seu Tempo Médio Diário de Estudo: ")
meta = input("Digite sua Principal Meta Atual: ")

print(f"""
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[NOME]................{nome}
[HORÁRIO].............{horario}
[MATÉRIA].............{materia}
[TEMPO DE ESTUDO].....{tmde}
[META]................{meta}
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")
