"""
Exercício 012

Peça uma temperatura em graus Celsius e exiba o valor convertido para Fahrenheit.
"""

# Seu código começa aqui

# (F = C * 1,8 + 32)
# (K = C + 273)

Celsius = float(input("Digite a temperatura em graus Celsius: "))

Fahrenheit = Celsius * 1.8 + 32
Kelvin = Celsius + 273.15

print(f"""
=-=-=-=-=-=-=-=-=-=-=-=
[FAHRENHEIT]...{Fahrenheit:.2f}
[KELVIN].......{Kelvin:.2f}
=-=-=-=-=-=-=-=-=-=-=-=""")