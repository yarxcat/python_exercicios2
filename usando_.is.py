#conhecendo funções (.is)
digite = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(digite) )

print('Só tem espaços? ', digite.isspace())
print('É um número? ', digite.isnumeric())
print('É alfabetico? ', digite.isalpha())
print('É alphanumerico? ', digite.isalnum())
print('Está em maiusculas? ', digite.isupper())
print('Está em minusculas? ', digite.islower())
print('Está capitalizada? ', digite.isidentifier())
