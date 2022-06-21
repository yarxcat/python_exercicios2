a = int(input('Digite um número: '))
ant = a - 1
suce = a + 1
d2 = a*2
d3 = a*3
r2 = a**(1/2)

print('O antecessor do numero digitado é {} e o seu sucessor é {}'.format(ant, suce))
print('O dobro de {} é {}, \n O triplo de {} é {} e sua raiz quadrada é {:.2f}'.format(a, d2, a, d3, r2))
