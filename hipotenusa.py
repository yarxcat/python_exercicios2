import angulo
ctop = float(input('Digite o numero do cateto oposto: '))
ctoadj = float(input('Digite o numero do cateto adjescente: '))
vlhipo = math.hypot(ctop, ctoadj)
print('O valor da hipotenusa é: {:.2f}'.format(vlhipo))