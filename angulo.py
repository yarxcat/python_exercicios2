import angulo
a = int(input('Digite o valor do angulo desejado: '))
cose = math.cos(math.radians(a))
seno = math.sin(math.radians(a))
tang = math.tan(math.radians(a))
print('O valor do cosseno de {}º é {:.2f}, {:.2f} é o seno e {:.2f} a tangente.'.format(a, cose, seno, tang))
