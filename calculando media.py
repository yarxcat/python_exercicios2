# exercicio 2
print('Resolvendo q2')

print('Calculando a media de suas notas')
nome = input('Digite seu nome: ')
n1 = float(input('Digite sua nota1: '))
n2 = float(input('Digite sua notas: '))
m = (n1+n2)/2

print('Olá {}, a média entre {} e {} foi de {:.1f}.'.format(nome, n1, n2, m))

if (m >= 6):
    print("Voce foi aprovado")
    print("Parabens")
else:
    if (m >= 5):
        print("Voce está de recuperação")

    if (m<5):
        print("Voce foi reprovado!!")
        print("Estude mais!")



