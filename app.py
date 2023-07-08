import requests

print('Hello World')


response = requests.get('https://predeepkumar-organic-fiesta-qp5xw75jrpq2x44w-8000.preview.app.github.dev/details')
data = response.json()
print(data)