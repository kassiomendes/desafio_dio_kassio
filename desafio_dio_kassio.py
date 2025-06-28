menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Digite o valor a ser depósitado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Falha na Operação! Valor inválido")

    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))

        saldo_excedido = valor > saldo

        limite_excedido = valor > limite

        saques_excedidos = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print("Falha na Operação! Saldo insuficiente.")

        elif limite_excedido:
            print("Falha na Operação! Limite de saque excedido.")

        elif saques_excedidos:
            print("Falha na Operação! Número de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Falha na Operação! Valor inválido.")

    elif opcao == "3":
        print("\n================EXTRATO================")
        print("_______________________________________")
        print("Nenhuma movimentação foi realizada." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n_______________________________________")
        print("=======================================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
