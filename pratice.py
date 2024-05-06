import requests

api_key = 'bd43aa0b-ce2a-4225-b80c-5f62ffa32a7c'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

print(definitions)

for definition in definitions:
    print(definition)
