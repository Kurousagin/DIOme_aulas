import textwrap
def menu():   
     menu = """\n
     =============== MENU ===============
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar Contas
    [nu] Novo Usuário
    [q] Sair
    =>"""  
     return input(textwrap.dedent(menu))

def deposito(saldo,valor,extrato, /):
     if valor > 0:
         saldo +=valor
         extrato += f"Depósito:\t\tR$ {valor:.2f}\n"
         print("\n==== Operação realizada com sucesso! ====")
     else:
         print("\n@@@ Operação falhou ! Valor inválido @@@")
     return saldo, extrato

def saque(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
        
        saldo_excedido = valor > saldo
        
        limite_excedido = valor > limite
        
        saque_excedido = numero_saques >= limite_saques

        if saldo_excedido:
            print("\n@@@ Saldo insuficiente!  @@@")
            
        elif limite_excedido:
            print("\n@@@ Operação falhou, limite de saque excedido! @@@")
            
        elif saque_excedido:
            print("\n@@@ Seu limite de saques foi excedido!@@@")
            
        elif valor > 0 :
            saldo -= valor
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            numero_saques +=1
            print("\n=== Operação realizada com sucesso! ===")
            
        else:
            print("\n@@@ Valor invalido!! @@@")
        
        return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):     
     
        print("<===================== EXTRATO ===========================>  "  )
        print( "Não fora realizada nenhuma movimentação" if not extrato else extrato)
        print(f"\n saldo :\t\tR$ {saldo:.2f}")
        print("<=========================================================>"    )


def cadastrar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente números): ")
    usuario = filtro_usuario(cpf, usuarios)
    if usuario:
        print("\n@@@ Usuário já extistente sob esse CPF! @@@")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço ( logradouro, nro - bairro - cidade/estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário cadastrado com sucesso! ===")

def filtro_usuario(cpf,usuarios):
    filtrados = [ usuario for usuario in usuarios if usuario["cpf"] == cpf ]
    return filtrados[0] if filtrados else None

def cadastrar_conta(AGENCIA, numero_conta,usuarios):
    cpf = input("informe o CPF do usuário: ")
    usuario = filtro_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado!! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta["usuario"]["nome"]}
       """
        print("#" * 100)
        print(textwrap.dedent(linha))
    




def main():
  LIMITE_SAQUES = 3
  AGENCIA = "0001"

  saldo = 0 
  limite = 500
  extrato = " "
  numero_de_saques = 0
  usuarios = []
  contas = []
  numero_conta = 1

  while True:

    opcao = menu()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: \n"))
        
        saldo, extrato = deposito(saldo,valor, extrato)
            
        
    elif opcao == "s":
        
        valor = float(input("INforme o valor de Saque: \n"))
        
        saldo, extrato = saque(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_de_saques,
            limite_saques=LIMITE_SAQUES,

        )

    elif opcao == "e":
      exibir_extrato(saldo, extrato=extrato)
      
    elif opcao == "lc":
            listar_contas(contas)

    elif opcao =="nu":
        cadastrar_usuario(usuarios)
    
    elif opcao == "nc":
        
        cadastrar_conta(AGENCIA, numero_conta, usuarios)

        if contas:
            contas.append(contas)
            numero_conta += 1

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione a operação desejada")


main()
     
        