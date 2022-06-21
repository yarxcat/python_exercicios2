a = float(input('Digite atemperatura em ºC para converter em ºF: '))
cf = (a* 9/5) + 32
b = float(input('Digite a temperatura em ºF para converter em ºC: '))
fc = (b -32)*5/9

print('O valor de {}ºC para ºF é de {}ºF.'.format(a, cf))
print('O valor de {}ºF convertido para ºC é de {}ºC.'.format(b, fc))
