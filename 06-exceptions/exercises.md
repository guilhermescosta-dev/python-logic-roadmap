# 06 - Exceptions

# Easy

## Exercício 067 - Tratando erro de conversão

Descrição:  
Peça um número inteiro ao usuário. Caso o usuário digite um valor inválido, exiba uma mensagem de erro em vez de quebrar o programa.

Foco:  
Uso básico de `try/except`.

Entrada:  
Um valor qualquer.

Saída:  
Número convertido ou mensagem de erro.

---

## Exercício 068 - Divisão segura

Descrição:  
Peça dois números ao usuário e exiba o resultado da divisão. Caso ocorra erro (como divisão por zero ou valor inválido), trate a exceção.

Foco:  
Tratamento de múltiplos erros.

Entrada:  
Dois números.

Saída:  
Resultado da divisão ou mensagem de erro.

---

## Exercício 069 - Entrada válida de inteiro

Descrição:  
Peça um número inteiro ao usuário até que ele digite um valor válido.

Foco:  
Loop + `try/except`.

Entrada:  
Tentativas do usuário.

Saída:  
Número válido convertido.

---

## Exercício 070 - Soma segura

Descrição:  
Peça dois números ao usuário e exiba a soma. Caso algum valor seja inválido, trate o erro e informe o problema.

Foco:  
Conversão com tratamento.

Entrada:  
Dois valores.

Saída:  
Soma ou mensagem de erro.

---

# Medium

## Exercício 071 - Menu com tratamento de erro

Descrição:  
Crie um menu simples com opções numéricas. Caso o usuário digite algo inválido (texto, número fora das opções), o programa deve tratar o erro e pedir novamente.

Foco:  
Validação + `try/except`.

Entrada:  
Opções do usuário.

Saída:  
Ação válida ou mensagem de erro.

---

## Exercício 072 - Divisão com repetição até válido

Descrição:  
Peça dois números ao usuário e tente realizar uma divisão. Caso ocorra erro, peça novamente os valores até que a operação seja válida.

Foco:  
Loop + tratamento de exceções.

Entrada:  
Tentativas do usuário.

Saída:  
Resultado válido da divisão.

---

## Exercício 073 - Lista de números com validação

Descrição:  
Peça ao usuário 5 números. Caso algum valor seja inválido, peça novamente apenas aquele número até que seja válido.

Foco:  
Validação individual com `try/except`.

Entrada:  
Cinco números válidos.

Saída:  
Lista completa de números.

---

## Exercício 074 - Conversão de múltiplos valores

Descrição:  
Peça três valores ao usuário e tente convertê-los para número. Caso algum falhe, informe qual valor foi inválido.

Foco:  
Identificação de erro específico.

Entrada:  
Três valores.

Saída:  
Conversões válidas ou mensagem indicando o erro.

---

## Exercício 075 - Soma com entrada interrompida

Descrição:  
Peça números ao usuário continuamente e some os valores válidos. Caso o usuário digite algo inválido, ignore e continue. O programa deve parar quando o usuário digitar "fim".

Foco:  
Tratamento + controle de fluxo.

Entrada:  
Números ou texto.

Saída:  
Soma dos valores válidos.

---

# Hard

## Exercício 076 - Validação completa de entrada

Descrição:  
Peça um número inteiro positivo. O programa deve garantir:

-   que o valor seja numérico
    
-   que seja inteiro
    
-   que seja positivo
    

Caso contrário, deve continuar pedindo até receber um valor válido.

Foco:  
Validação completa com exceções.

Entrada:  
Tentativas do usuário.

Saída:  
Número válido.

---

## Exercício 077 - Sistema de login com tentativas limitadas

Descrição:  
Crie um sistema de login com senha. O usuário tem no máximo 3 tentativas. Caso digite algo inválido ou erre a senha, o programa deve tratar e continuar até o limite.

Foco:  
Exceção + controle de tentativas.

Entrada:  
Tentativas de senha.

Saída:  
Acesso permitido ou bloqueado.

---

## Exercício 078 - Calculadora segura

Descrição:  
Crie uma calculadora que recebe dois números e uma operação. O programa deve tratar:

-   entrada inválida
    
-   divisão por zero
    
-   operação inválida
    

Foco:  
Múltiplas exceções.

Entrada:  
Dois números e uma operação.

Saída:  
Resultado ou mensagem de erro.

---

## Exercício 079 - Média com validação contínua

Descrição:  
Peça várias notas ao usuário. Caso alguma seja inválida, peça novamente até que todas sejam válidas. Ao final, calcule a média.

Foco:  
Validação contínua.

Entrada:  
Notas válidas.

Saída:  
Média das notas.

---

## Exercício 080 - Conversão dinâmica com tratamento

Descrição:  
Peça um valor ao usuário e tente convertê-lo para inteiro. Se não for possível, tente converter para decimal. Caso nenhuma conversão seja possível, informe erro.

Foco:  
Múltiplas tentativas de conversão.

Entrada:  
Um valor.

Saída:  
Valor convertido ou mensagem de erro.