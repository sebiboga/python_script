import requests
import json

# URL-ul API-ului
url = "https://api.peviitor.ro/v5/get_token/"

# Payload-ul pe care dorim să-l trimitem
payload = {
    "email": ""
}

# Header-ul pentru cererea POST
headers = {
    "Content-Type": "application/json"
}

# Efectuarea cererii POST
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Verificarea răspunsului
if response.status_code == 200:
    print("Cererea a fost efectuată cu succes!")
    print("Răspuns:", response.json())
else:
    print("A apărut o eroare:", response.status_code, response.text)
