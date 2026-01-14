saque = float(input("Digite o valor do saque: "))

limite = float (1000.00)
if saque > limite:
    print("Saldo insuficiente para saque.")

elif saque % 10 == 0:
    print("Saque realizado com sucesso!") 

else:
    print("O caixa só possui notas de 10.")

#Condição Simples: O if verifica se o saque é maior que o limite. Se for, exibe a mensagem de saldo insuficiente.
#Condição Composta: O elif verifica se o saque é múltiplo de 10. Se for, o saque é realizado com sucesso. Caso contrário, a mensagem indica que o caixa só possui notas de 10.


