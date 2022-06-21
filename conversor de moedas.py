# crie um programa que mostre para pessoa quanto ela tem na carteira e quanto ficaria em dólares

nome = input('Digite seu nome: ')
print('Olá', nome, '!! ')
saldo = float(input('Digite seu saldo em R$: '))

# 1 realBr é igual a 0,20 doll/ 1 Euro == 0,19
doll = (saldo * 0.20)
eur = (saldo * 0.19)

print('{}, seu saldo de {}R$ convertido para o dollar americano é de {}$'.format(nome, saldo, doll))
print('Convertendo em Euro fica: {}Euros'.format(eur))
print('{}, isso significa que voce pode comprar {} dolares ou {} euros.'.format(nome,doll, eur))


