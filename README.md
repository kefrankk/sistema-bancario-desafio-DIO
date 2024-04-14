# 🏦 Sistema bancário - Desafio DIO


Este projeto foi desenvolvido como parte do Bootcamp **Python AI Backend Developer** na DIO, com o objetivo de aplicar e aprimorar os conhecimentos em Python adquiridos durante o curso.


### ✅ Funcionalidades

1. 💰 **Depósito:** Permite aos usuários realizar depósitos em suas contas bancárias.
2. 💸 **Saque:** Os usuários podem fazer até 3 saques por dia, com um limite máximo de R$ 500,00 por operação.
3. 📜 **Extrato:** Exibe o extrato da conta bancária do usuário, mostrando o histórico de transações.
4. 🆕 **Nova conta corrente:** Permite aos usuários que possuem cadastro criar novas contas bancárias.
5. 👤 **Novo usuário:** Realiza o cadastro de novos usuários no sistema.
6. ❌ **Deletar conta corrente:** Permite aos usuários que possuem cadastro deletar suas contas bancárias.


### ✅ Como Executar

Para executar o projeto localmente, siga as etapas abaixo:

1. Clone o repositório.
2. Execute o arquivo principal do sistema bancário.


### ✅ Condições do desafio

Esse desafio é dividido em várias partes, conforme se avança no Bootcamp. A seguir, são listadas as condições para a criação do sistema bancário por etapas.

- **Etapa 1:** Criar um código que implementa três operações principais: depósito, saque e extrato. 
    -- *Depósito*: Os depósitos devem ser armazenados em uma variável e exibidos no extrato.
    -- *Saque*: O sistema deve permitir ate 3 saques por dia, com um limite máximo de R$ 500,00 por operação. Caso o usuário não tenha saldo, o sistema deve exibir uma mensagem informando que não há dinheiro suficiente disponível para a operação. Todos saques devem ser armazenados em uma variável e exibidos no extrato.
    -- *Extrato*: Esta operação deve listar todos os depósitos e saques realizados pelo usuário. No final, deve mostrar o saldo atual no formato R$ xxx.xx. 

- **Etapa 2:** Criar funções para cada operação da Etapa 1 e criar novas funções para criar nova conta corrente e novo usuário.
    -- *Depósito*: A função deve receber argumentos apenas por posição. Sugestão de argumentos: saldo, valor, extrato. Sugestão de retorno: saldo, extrato.
    -- *Saque*: A função deve receber argumentos apenas por nome. Sugestão de argumentos: saldo, valor, extrato, limite, numero de saques, limite de saques. Sugestão de retorno: saldo e extrato. 
    -- *Extrato*: A função deve receber argumentos por posição e por nome. Sugestão de argumentos: extrato. Sugestão de retorno: extrato. Argumento posicional: saldo. Argumento nomeado: extrato.
    -- *Criar novo usuário*: Realiza o cadastro de novos usuários. A função deve armazenar os usuários em uma lista. Um usuário é composto por: nome, data de nascimento, CPF e endereço. O endereço deve ser uma string no formato: logradouro, número - bairro - cidade/sigla estado. Deve ser armazenado somente o numero de CPF (formato string), pois não podem ser cadastrados dois usuários com o mesmo CPF. 
    -- *Criar nova conta corrente*: Permite aos usuários que possuem cadastro criar novas contas bancárias. O sistema deve armazenar as contas em uma lsita. Uma conta é composta por: agência, numero da conta, usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: '0001'. O usuário pode ter mais de uma conta, mas uma conta pertence a somente um usuário. 

