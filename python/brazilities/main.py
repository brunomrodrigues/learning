import requests 
from adress import Adress 
adress = Adress("11055340")

request = requests.get("https://viacep.com.br/ws/{}/json".format(adress.cep))
response = request.json()

adress.neighborhood = response.get("bairro")
adress.street = response.get("logradouro")

print(adress)