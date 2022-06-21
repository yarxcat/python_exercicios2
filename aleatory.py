import random
print('Olá, digite o nome de seus alunos abaixo para sortear quem vai apagar o quadro!!')
a1 = str(input('Digite um nome:'))
a2 = str(input('Digite um nome: '))
a3 = str(input('Digite um nome: '))
a4 = str(input('Digite um nome: '))
lista = [a1, a2, a3, a4]
print('O aluno sorteado para apagar o quadro  foi {}'.format(random.choice(lista)))

print('Agora iremos sortear quem ira apresentar primeiro: ')
random.shuffle(lista)
print(lista)
