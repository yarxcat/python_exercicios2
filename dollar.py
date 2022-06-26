#buscando o valor do dollar
import requests

# link publico com o valor atual do dollar
url = 'https://economia.awesomeapi.com.br/all/USD-BRL'

# busca de dados
response = requests.get(url)

# se a busca funcionou, mostra valor
if response.status_code == 200:
    dolar_value = response.json()['USD']['low']
    print( f'O valor do dólar éR$ {dolar_value}')
else:
    print('Erro ao buscar valor do dollar')
