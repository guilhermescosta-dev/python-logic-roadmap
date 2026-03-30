# 10 - Mixed Challenges

# Easy

## Exercício 123 - Lista de tarefas com gerenciamento

Preciso de um programa simples para organizar tarefas do dia a dia da equipe.

Não quero só digitar tarefas e mostrar no final. Quero algo minimamente útil.

O sistema deve permitir:

-   adicionar novas tarefas
    
-   listar todas as tarefas cadastradas
    
-   marcar uma tarefa como concluída
    
-   remover uma tarefa
    
-   encerrar o programa quando o usuário quiser
    

As tarefas podem ficar armazenadas apenas enquanto o programa estiver rodando, não precisa salvar em arquivo.

Quero algo feito no terminal, com menu, mas que funcione de forma organizada.

---

## Exercício 124 - Registro de gastos pessoais com resumo

Quero um sistema básico para registrar gastos do dia a dia.

A pessoa deve conseguir:

-   cadastrar um gasto com descrição e valor
    
-   listar os gastos cadastrados
    
-   ver o total gasto até o momento
    
-   ver qual foi o maior gasto
    
-   encerrar quando quiser
    

Não precisa usar banco de dados nem arquivo, mas durante a execução do programa as informações precisam ficar armazenadas.

Também preciso que o sistema trate entradas inválidas sem quebrar.

---

## Exercício 125 - Sistema de fila de atendimento

Preciso de um sistema simples para organizar atendimento.

A ideia é:

-   pessoas entram na fila informando o nome
-   o sistema deve permitir chamar a próxima pessoa
-   também deve permitir visualizar quem está na fila

Não precisa nada avançado, mas precisa funcionar de forma consistente.

Detalhe importante:  
quem entra primeiro deve ser atendido primeiro.

---

# Medium

## Exercício 126 - Sistema de notas com múltiplos alunos

Preciso de um sistema em terminal para ajudar um professor a organizar as notas dos alunos.

O programa deve permitir cadastrar vários alunos. Para cada aluno, serão informadas duas notas, referentes a duas unidades.

O professor precisa conseguir:

-   cadastrar um novo aluno
    
-   editar as notas de um aluno já existente
    
-   listar todos os alunos com suas notas
    
-   exibir a média de cada aluno
    
-   mostrar quais alunos estão aprovados e quais estão reprovados
    

A regra de aprovação pode ser definida como média maior ou igual a 7.

O sistema deve continuar funcionando em menu até o professor decidir sair.

O mais importante aqui não é aparência, é organização da lógica.

---

## Exercício 127 - Cadastro de produtos com análise simples

Um pequeno comerciante quer um sistema em terminal para controlar produtos.

Cada produto deve ter pelo menos:

-   nome
    
-   preço
    
-   quantidade em estoque
    

O sistema deve permitir:

-   cadastrar novos produtos
    
-   editar preço ou quantidade de um produto já existente
    
-   listar todos os produtos
    
-   mostrar o valor total do estoque
    
-   identificar o produto mais caro
    
-   identificar o produto com maior quantidade
    

Tudo pode ficar na memória enquanto o programa roda.

O sistema precisa ser prático, sem travar quando o usuário digitar algo inválido.

---

## Exercício 128 - Sistema de ranking de jogadores

Quero um sistema simples para registrar pontuação de jogadores.

O programa deve permitir:

-   cadastrar jogadores com nome e pontuação
-   atualizar a pontuação de um jogador existente
-   listar os jogadores ordenados da maior pontuação para a menor

Não precisa interface bonita, mas a lógica precisa estar correta.

O ranking deve sempre refletir o estado atual dos dados.

---

# Hard

## Exercício 129 - Sistema de login com usuários e bloqueio

Preciso de um sistema simples de acesso para vários usuários.

Cada usuário deve ter:

-   nome de usuário
    
-   senha
    
-   contador de tentativas erradas
    
-   status de bloqueio
    

O programa deve permitir:

-   cadastrar usuários
    
-   fazer login
    
-   bloquear automaticamente um usuário após 3 tentativas erradas
    
-   listar usuários cadastrados
    
-   mostrar quais usuários estão bloqueados
    

Não precisa salvar em arquivo, mas tudo deve funcionar corretamente durante a execução.

Quero algo bem controlado, porque a lógica de autenticação precisa estar consistente.

---

## Exercício 130 - Simulador de caixa eletrônico com cédulas

Agora preciso de um simulador de caixa eletrônico mais realista.

O sistema deve começar com:

-   um saldo disponível para o cliente
    
-   uma quantidade de cédulas no caixa, por exemplo de 100, 50, 20 e 10
    

O programa deve ter menu e permitir:

-   consultar saldo
    
-   depositar valor
    
-   sacar valor
    
-   encerrar
    

No saque, não basta só diminuir o saldo.

O sistema precisa calcular quais cédulas serão entregues, levando em conta:

-   o valor solicitado
    
-   a quantidade de cédulas disponível no caixa
    
-   as combinações possíveis no momento
    

Exemplo:  
se o cliente pedir 500, o sistema pode talvez entregar:

-   5 cédulas de 100
    

ou

-   10 cédulas de 50
    

Mas isso depende do estoque atual do caixa.

Cada saque altera o número de cédulas disponíveis, então as possibilidades mudam ao longo do uso.

Se não for possível montar o valor com as cédulas restantes, o saque deve ser negado, mesmo que o cliente tenha saldo.

Entradas inválidas não podem quebrar o sistema.

O gerente deixou claro que quer um sistema funcional e bem pensado, mesmo sendo em terminal.

---

## Exercício 131 - Calculadora de binário (sem conversão para decimal)

Preciso de uma calculadora que some dois números binários.

Exemplo:

-   1011 + 0011

Mas tem uma regra MUITO IMPORTANTE:

Você **não pode converter para decimal** em nenhum momento.

Ou seja:

-   não pode usar `int(x, 2)`
-   não pode transformar em base 10 para resolver

Você deve simular exatamente o que acontece no papel:

-   soma bit a bit
-   da direita para esquerda
-   tratando o "vai um" (carry)

O sistema deve:

-   receber dois números binários
-   validar se são binários válidos
-   realizar a soma manualmente
-   exibir o resultado final em binárioPreciso de uma calculadora que some dois números binários.
-   Exemplo:
    
-   1011 + 0011
-   Mas tem uma regra MUITO IMPORTANTE:
    
-   Você **não pode converter para decimal** em nenhum momento.
    
-   Ou seja:
    
-   não pode usar `int(x, 2)`
-   Você deve simular exatamente o que acontece no papel:
    
-   soma bit a bit
-   tratando o "vai um" (carry)
-   O sistema deve:
    
-   receber dois números binários
-   realizar a soma manualmente