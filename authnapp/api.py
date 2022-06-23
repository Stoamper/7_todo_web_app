import requests

response = requests.post('http://127.0.0.1:8000/api-token-auth/', 
data={'username': 'stoamper', 'password': '33Cltkfk'})

print(response.status_code)
print(response.json())

# Работает только если пользователь уже есть в системе (для stoamper работает)