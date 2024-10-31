import textwrap

def menu():
    menu = """ 
    Digite o Número da Operação Desejada:

    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova Conta
    [5]\tListar Contas
    [6]\tNovo Usuário
    [0]\tSair
    ======================================
    :"""
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if(valor <= 0):
        print("Operação não Realizada!,Digite um valor valido para o depósito")
    else:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\nDepósito Realizado com sucesso")
        print("=" * 10)
    
    return saldo, extrato
        
def sacar(*, saldo, valor, extrato, saques):
    #Regra de negocio,limite de saques diarios igual a 3,NÃO MODIFICAR
    if(valor <= 0 or valor > 500 or valor > saldo or saques >= 3):
        if(valor <= 0):
            print("Operação não Realizada!,Digite um valor valido para o saque")
            print("=" * 10)
        elif(valor > 500):
            print("Operação não Realizada!,O Valor Limite para Saques é de R$500.00")
            print("=" * 10)
        elif(valor > saldo):
            print("Operação não Realizada!,Saldo insuficiente")
            print("=" * 10)
        elif(saques >= 3):
            print("Operação não Realizada!,Só possivel realizar 3 saques por dia")
            print("=" * 10)
    else:
        saldo -= valor
        extrato += f"Saque:\tR$ {valor:.2f}\n"
        saques += 1
        print("Saque Realizado com sucesso")
        print("=" * 10)
    
    return saldo, extrato, saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n====Extrato da sua Conta====")
    print(" " if not extrato else extrato)
    print(f"\nSaldo:\tR$ {saldo:.2f}")
    print("==============================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if(usuario):
        print("Já existe usuário com esse CPF")
        print("=" * 10)
        return
    
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento (dd-mm-aaa): ")
    endereco = input("Digite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "enreço": endereco})
    
    print("Usuário criado com sucesso")
    print("=" * 10)
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if(usuario):
        print("\nConta criada com sucesso.\nBem vindo ao nosso Banco")
        print("=" * 10)
        return {"agencia": agencia, "numero_conta": numero_conta, "usuário": usuario}
    
    print("Usuário não encontrado,crie um usuário para poder criar uma conta!!")
    print("=" * 10)

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuário']['nome']}
        """
        print("=" * 50)
        print(textwrap.dedent(linha))

def main():
    AGENCIA = "0001"
    
    saldo = 0
    extrato = ""
    saques = 0
    usuarios = []
    contas = []
    print("====   Bem Vindo ao Banco   ====")
    while(True):
        op= int(menu())
    
        if(op == 1):
            print("Informe o Valor a ser Depositado:")
            valor = float(input())
            
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif(op == 2):
            print("informe o Valor a Ser Sacado:")
            valor = float(input())
            
            saldo, extrato, saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                saques=saques
            )
        
        elif(op == 3):
            exibir_extrato(saldo, extrato=extrato)
        
        elif(op == 4):
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
        
        elif(op == 5):
            listar_contas(contas)
        
        elif(op == 6):
            criar_usuario(usuarios)
        
        
        elif(op == 0):
            print("Obrigado por usar o nosso Banco!")
            break
        
        else:
            print("Operação Invalida!")
  
   
main()