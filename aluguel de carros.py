days = int(input('Digite a quantidade de dias que o carro ficou alugado? '))
km = float(input('Digite a quantidade de KM rodados? '))
d = days*60
k = km*0.15
dk = d+k
print('O valor a se pagar pelo aluguel é {}R$'.format(dk))