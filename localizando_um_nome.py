#manipulação de str
#exercicio para localizar uma palavra em qualquer posição da frase
nm = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem silva? {}'.format('silva' in nm.lower()))
