# calculando a quantidade de tinta necesaria

n1 = float(input('Digite a altura da parede(m²): '))
n2 = float(input('Digite a largura da parede(m²): '))
n3 = float(input('Digite em metros quanto a sua tinta rende por L:'))
cal = (n1*n2)/n3
a = n1*n2
print('A área da sua parede é de {}m²'.format(a))
print('A tinta que voce possui rende {} m² por litros, por tanto voce irá precisar de {}L'.format(n3, cal))


