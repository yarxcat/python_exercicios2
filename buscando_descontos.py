#encontra descontos digitando o valor do produto
print('Buscando descontos')
a = float(input('Digite o valor do produto desejado: '))
# desconto de 5%
desc5 = a - (a*0.05)
# desconto de 10%
desc10 = a - (a*0.1)
# desconto de 15%
desc15 = a - (a*0.15)
# desconto de 20%
desc20 = a - (a*0.2)

print('O valor do seu do produto escolhido fica {}R$, com 5% de desconto.'
      '{}R$, com 10% de desconto. {}R$ com 15% e {}R$ com 20%'.format(desc5, desc10, desc15, desc20))
print('Consulte o caixa para pode saber quais descontos estão didponiveis para você!!')
