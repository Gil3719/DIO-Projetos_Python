saldo = 0
limite_saque = 500
saques = 0
lista_saques = []
lista_deposito = []


print("Bem Vindo ao Banco")
menu =(""" 
 Digite o Número da Operação Desejada:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
""")

while(True):
    print(menu)
    op= int(input())
    
    if(op == 1):
        print("Informe o Valor a Depositado:")
        valor = float(input())
        if(valor <= 0):
            print("Operação não Realizada!,Digite um valor valido para o depósito")
        else:
            saldo += valor
            lista_deposito.append(f"R$ {valor:.2f}")
            print("Depósito Realizado com sucesso")
    
    elif(op == 2):
        print("informe o Valor a Ser Sacado:")
        valor = float(input())
        #Regra de negocio,limite de saques diarios igual a 3,NÃO MODIFICAR
        if(valor <= 0 or valor > 500 or valor > saldo or saques >= 3):
            if(valor <= 0):
                print("Operação não Realizada!,Digite um valor valido para o saque")
            elif(valor > 500):
                print("Operação não Realizada!,O Valor Limite para Saques é de R$500.00")
            elif(valor > saldo):
                print("Operação não Realizada!,Saldo insuficiente")
            elif(saques >= 3):
                print("Operação não Realizada!,Só possivel realizar 3 saques por dia")
        else:
            saldo -= valor
            lista_saques.append(f"R$ {valor:.2f}")
            saques += 1
            print("Saque Realizado com sucesso")
    
    elif(op == 3):
        print(f"""====Extrato da Sua Conta===:
        
    Depositos:
    {lista_deposito}      
        
        
    Saques:
    Saques Realizados: {saques} 
    {lista_saques}
        
        
    Seu Saldo: R${saldo:.2f}
==============================""")

    
    elif(op == 0):
        print("Obrigado por usar o nosso Banco!")
        break
    
    else:
        print("Operação Invalida!")