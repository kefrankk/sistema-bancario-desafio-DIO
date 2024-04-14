"""
Sistema bancário - Desafio DIO


by Kelly Heckler
"""

import re
import textwrap
import numpy as np
import pandas as pd
from datetime import datetime

arquivo_clientes = 'clientes.csv'


def menu():
    
    mensagem = """
    ========= MENU =========

    Bem vindo(a)!

    Escolha a operação desejada:

    [1] Depósito               [2] Saque 
    [3] Extrato                [4] Nova conta corrente
    [5] Novo usuário           [6] Deletar conta corrente
    [0] Sair

    ========================
    """
    return input(mensagem)


def data_atual():
    return datetime.now().strftime("%d/%m/%Y")


def deposito(valor, saldo, extrato):

    if valor > 0:
        saldo += valor
        extrato += f" {data_atual()} - Depósito de R$ {valor:.2f} \n"
        print(f"Depósito de R$ {valor:.2f} efetuado com sucesso!")

    return saldo, extrato


def sacar(*, valor, saldo, extrato, limite, numero_saques, SAQUE_DIARIO):
        
    if numero_saques > SAQUE_DIARIO - 1:
        print("Limite de saques diário excedido.")
        
    elif valor > limite:
        print(f"O valor R$ {valor:.2f} ultrapassa o limite de R$ {limite:.2f}!")

    elif valor > saldo:
        print("Saldo insuficiente!")

    else:
        if valor > 0:
            saldo -= valor
            extrato += f"{data_atual()} - Saque de R$ {valor:.2f}\n"
            print(f"Saque de R$ {valor:.2f} efetuado com sucesso!")
    
    return saldo, extrato


def Extrato(saldo, *, extrato):
    print(" ########### Extrato ########### \n")
    print('Não foram realizadas movimentações. \n' if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")


def listar_cliente(usuarios):
    return (cliente['cpf'] for cliente in usuarios)


def listar_conta(conta_corrente):    
    return (conta['numero_conta'] for conta in conta_corrente)


def informe_cpf():

    cpf = input("Por favor, informe seu CPF: ")

    while len(cpf) != 11:
        print("CPF deve ter 11 dígitos. Ignore pontos e hífen. \n")
        cpf = input("Por favor, informe seu CPF: ")

    return str(cpf)


def validar_endereco(endereco):

    padrao = r'^[\w\s]+\,\s\d+\s\-\s[\w\s]+\s\-\s[\w\s]+\/[A-Z]{2}$'

    if len(endereco) > 10 and len(endereco) < 100:
        return re.fullmatch(padrao, endereco) is not None
    else:
        return False
    


def validar_data_nascimento(data_nascimento):
    if len(data_nascimento) == 8:

        try:
            data = datetime.strptime(data_nascimento, '%d%m%Y')
            hoje = datetime.now()

            if data < hoje:
                return True
            else:
                return False

        except ValueError:
            return False

        
def criar_usuario(cpf, usuarios):

    cliente = listar_cliente(usuarios)

    if cpf not in cliente:#:
        nome = input("Digite seu nome completo: ")
        data_nascimento = input("Digite sua data de nascimento (ddmmaaaa): ")

        # validando a data de nascimento
        while validar_data_nascimento(data_nascimento) == False:
            print("Data de nascimento inválida. \n ")
            data_nascimento = input("Digite sua data de nascimento (ddmmaaaa): ")

        data_nascimento = datetime.strptime(data_nascimento, '%d%m%Y').strftime('%d/%m/%Y')
        
        endereco = input("Digite seu endereço (logradouro, numero - bairro - cidade/sigla estado): ")

        # validando o formato do endereço
        while validar_endereco(endereco) == None or validar_endereco(endereco) == False:
            print("Endereço inválido. Tente novamente. \n")
            endereco = input("Digite seu endereço (logradouro, numero - bairro - cidade/sigla estado): ")
                  
        usuarios.append({'cpf': cpf, 
                         'nome': nome, 
                         'data_nascimento': data_nascimento, 
                         'endereço': endereco})
        print('Novo usuário cadastrado com sucesso! \n') 

    else:
        print('Usuário já cadastrado. \n')


    

def criar_conta_corrente(numero_conta, agencia, conta_corrente, usuarios):    
    
    cpf = informe_cpf()
    cliente = listar_cliente(usuarios) 
    conta = listar_conta(conta_corrente) 

    if cpf in cliente:
        nome = next(cliente['nome'] for cliente in usuarios if cliente['cpf'] == cpf)
        print(f"Bem vindo(a), {nome}! \n")

    else:
        print( 'Usuário não cadastrado. Crie uma conta de usuário. \n')
        return False


    if numero_conta not in conta: 
        conta_corrente.append({'numero_conta': str(numero_conta), 
                               'agencia': agencia, 
                               'cpf': cpf,
                               'nome': nome})
        
        print("Conta corrente criada com sucesso! \n")

    else:
        print('Conta corrente já existe. \n')


    return numero_conta, agencia, cpf
    

def checar_numero_conta(cpf, conta_corrente):
    return (conta for conta in conta_corrente if conta['cpf'] == cpf)

def listar_contas_por_cpf(cpf, conta_corrente):
    contas_encontradas = []
    for conta in conta_corrente:
        if conta.get('cpf') == cpf:
            contas_encontradas.append(conta)

    return contas_encontradas

def deletar_conta_corrente(cpf, usuario, conta_corrente):
    
    contas_associadas = listar_contas_por_cpf(cpf, conta_corrente)

    if not contas_associadas:
        print("Nenhuma conta encontrada para este CPF.")
        return False
    

    for i, conta in enumerate(conta_corrente):
        if len(contas_associadas) == 1 and conta.get('cpf') == cpf:
            del conta_corrente[i]
            print("Conta corrente excluída com sucesso! \n")
            
            print("Deseja deletar o usuário associado? \n")
            deletar_usuario = int(input("[1] Sim \n[2] Não \n \n"))

            if deletar_usuario == 1:
                del usuario[i]
                print("Usuário excluído com sucesso! \n")

            elif deletar_usuario == 2:
                return False

        elif len(contas_associadas) > 1 and conta.get('cpf') == cpf:
            print(f"Contas associadas ao CPF {cpf}:")

            for j, contas in enumerate(contas_associadas, start=1):
                print(f"[{j}] {contas}")

            escolha = input("Digite o número da conta que deseja deletar: ")

            if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(contas_associadas):
                print("Escolha inválida.")
                return False
                
            # Remover a conta escolhida da lista de contas correntes
            conta_corrente.remove(contas_associadas[int(escolha) - 1])
            print("Conta corrente excluída com sucesso!")

            return False




def main():

    AGENCIA = '0001'
    SAQUE_DIARIO = 3
    
    saldo = 0
    extrato = ""
    limite = 500
    numero_saques = 0
    conta_corrente = []
    usuarios = []



    while True:

        operacao = menu()


        if operacao == '1':
            valor = float(input("Quanto deseja depositar? "))

            saldo, extrato = deposito(valor, saldo, extrato)


        elif operacao == '2':
            quantia = float(input("Quanto deseja sacar? "))

            saldo, extrato = sacar(valor = quantia, 
                                   saldo = saldo, 
                                   extrato = extrato, 
                                   limite = limite, 
                                   numero_saques = numero_saques, 
                                   SAQUE_DIARIO = SAQUE_DIARIO
                                   )

            numero_saques += 1


        elif operacao == '3':
            Extrato(saldo, extrato = extrato)


        elif operacao == '4':
            numero_conta = str(len(conta_corrente) + 1)

            criar_conta_corrente(numero_conta = numero_conta,
                                 agencia = AGENCIA, 
                                 conta_corrente = conta_corrente, 
                                 usuarios = usuarios)


        elif operacao == '5':
            cpf = informe_cpf()
            criar_usuario(cpf, usuarios)


        elif operacao == '6':
            cpf = informe_cpf()
            deletar_conta_corrente(cpf, usuarios, conta_corrente)


        elif operacao == '0':
            break


        else:
            print("Operação inválida, tente novamente!")


main()
