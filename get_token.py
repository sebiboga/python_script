import requests
import json
import sys

# Verificăm dacă a fost furnizat un email
if len(sys.argv) < 2:
    print("Te rog să furnizezi un email ca argument.")
    sys.exit(1)

email = sys.argv[1]

# URL-ul API-ului
url = "https://api.peviitor.ro/v5/get_token/"

# Payload-ul pe care dorim să-l trimitem
payload = {
    "email": email
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
    
    # Răspunsul JSON
    response_data = response.json()
    print("Răspuns:", response_data)
    
    # Extracția token-ului
    if 'token' in response_data:
        token = response_data['token']
        print("Token-ul extras este:", token)
    else:
        print("Token-ul nu a fost găsit în răspuns.")
else:
    print("A apărut o eroare:", response.status_code, response.text)
