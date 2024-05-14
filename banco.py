menu = '''

 [d] Depositar
 [s] Sacar
 [e] Extrato
 [q] Sair

'''

saldo = 1000
limite = 500
extrato = '''
'''
numero_saques = 0
LIMITE_SAQUES = 3
numero_depositos = 0
depositos = []
saques = []

while True :
    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Quanto você deseja depositar? "))
        if deposito < 0.01:
            print(f"Operação invalida, por favor digite um valor positivo!")
        else:
            depositos.append(f"R$ {deposito:.{2}f}")
            numero_depositos += 1
            saldo += deposito
            print(f"Depostio realizado com sucesso, seu saldo atual é de R$ {saldo:.{2}f} ")

    elif opcao == "s":
        if numero_saques >= LIMITE_SAQUES:
            print("Seu limite diário de saques foi atingido")
        else:
            saque = float(input("Quanto você deseja sacar? "))
            if saque < 0.01:
                print("Por favor digite um valor válido")
            elif saque > limite:
                print("Você está tentanto sacar um valor maior do que o permitido, o seu limite por saque é de R$ 500.00 reais")
            elif saque > saldo:
                print("Erro! Você está tentando sacar um valor acima do seu saldo")
            else:
                saques.append(f"R$ {saque:.{2}f}")
                saldo -= saque
                numero_saques += 1
                print(f"Saque realizado com sucesso, seu saldo atual é de R$ {saldo:.{2}f}")
        

    elif opcao == "e":
        extrato = f'''
        {"EXTRATO".center(20)}

        Você realizou {numero_depositos} depositos nos valores de {depositos} respectivamente
        Você realizou {numero_saques} saques nos valores de {saques} respectivamente

        Seu saldo atual é de R$ {saldo:.{2}f}
        '''
        print(extrato)

    elif opcao == "q":
        break

    else:
        print("Operação inválida!")

print("você finalizou sua operação!")