"""
Exercício 016

Peça o preço de um produto e um valor de desconto (em porcentagem). Calcule o valor final com o desconto aplicado.
"""

# Seu código começa aqui

preco = float(input("Digite o Preço do Produto: R$"))
desconto = float(input("Digite o PERCENTUAL [%] de Desconto: "))

novopreco = preco - (preco*desconto/100)

print(f"Este Produto com o desconto ficou: R${novopreco:.2f}")