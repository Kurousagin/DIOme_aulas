menu = """
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=>"""


saldo = 0 
limite = 500
extrato = ""
# permite apenas 3 saques diarios/ ARMAZENAR A QUANTIDADE DE SAQUES
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "D":
        valor = float(input("Informe o valor do depósito: \n"))
        
        if valor > 0:
            saldo += valor
            extrato += f" Depósito: R$ {valor:.2f}\n"
            # extrato += valor
            # value = f" Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação falhou! Valor informado invalido")
            
        
    elif opcao == "S":
        
        valor = float(input("INforme o valor de Saque: \n"))
        
        saldo_excedido = valor > saldo
        
        limite_excedido = valor > limite
        
        saque_excedido = numero_saques >= LIMITE_SAQUES
        
        if saldo_excedido:
            print("Saldo insuficiente ")
            
        elif limite_excedido:
            print("Operação falhou, limite de saque excedido!")
            
        elif saque_excedido:
            print("Seu limite de saques foi excedido!")
            
        elif valor > 0 :
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques +=1
            
        else:
            print("Valor invalido!!")
            
        # if (saldo > 0):
        #     saque = int(input("Qual valor deseja sacar? : \n"))
        #     print("\n" * 130)
        # if (saldo >= saque):
        #     saldo = saldo - saque
        #     # LIMITE POR SAQUE = $500 , CASO NÃO TENHA SALDO, EXIBIR MENSAGEM
        #     print('SEU SALDO ATUAL É: ', saldo)
        # else:
        #     print('saldo insuficiente')

            
    elif opcao == "E":
        # exibir variavel de extrato, formatada já em valores
        print("<=====================menu===========================>  "  )
        print( "Não fora realizada nenhuma movimentação" if not extrato else extrato)
        print(f"\n saldo : R$ {saldo:.2f}")
        print("<===================================================>"    )
    elif opcao == "Q":
        break

    else:
        print("Operação invalida, por favor selecione a operação desejada")



