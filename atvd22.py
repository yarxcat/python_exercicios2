# atividade 022

nome = str(input('Digite seu primeiro e segundo nome: '))
print('Analiando seu nome...')
div = nome.split()
print("""Seu nome em maiusculas é {}
Seu nome em minusculas é {}
Seu primeiro nome tem {} letras. 
Seu nome completo tem {} letras.""".format(nome.upper(), nome.lower(), len(div[0]), len(div[0])+len(div[1])))


