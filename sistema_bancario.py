"""
Sistema bancário simples - Desafio DIO
"""


menu = """

    Bem vindo!

    Escolha a operação desejada:

    [1] Depósito
    [2] Saque
    [3] Extrato 
    [0] Sair

"""

# definindo as variaveis
saldo = 0
extrato = ""
limite = 500
numero_saques = 0
SAQUE_DIARIO = 3



while True:

    operacao = float(input(menu))


    if operacao == 1:
        valor = float(input("Quanto deseja depositar? "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} efetuado com sucesso!")


    elif operacao == 2:
        quantia = float(input("Quanto deseja sacar? "))
        
        if numero_saques > SAQUE_DIARIO:
            print("Limite de saques diário excedido.")
            
        
        elif quantia > limite:
            print(f"O valor R$ {quantia:.2f} ultrapassa o limite de R$ {limite:.2f}!")

        elif quantia > saldo:
            print("Saldo insuficiente!")

        else:
            if quantia > 0:
                saldo -= quantia
                extrato += f"Saque de R$ {quantia:.2f}\n"
                print(f"Saque de R$ {quantia:.2f} efetuado com sucesso!")
                numero_saques += 1


    elif operacao == 3:
        print()
        print(" ########### Extrato ########### \n")
        print('Não foram realizadas movimentações. \n' if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")


    elif operacao == 0:
        break


    else:
        print("Operação inválida, tente novamente!")

