'''
Você recebe uma entrada de número e precisa verificar se é um número de telefone válido. 
Um número de telefone válido tem exatamente 8 dígitos e começa com 1, 8 ou 9. 
Saída "Válido" se o número for válido e "Inválido", se não for
'''

import re
#your code goes here
num = input()

pathern = re.compile(r"^(1|8|9)(\d){7}$")

if pathern.search(num):
    print("Valid")
else:
    print("Invalid")
