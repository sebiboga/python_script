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

# Header-ul pentru cererea POST, inclusiv User-Agent
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Efectuarea cererii POST
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Verificarea răspunsului
if response.status_code == 200:
    print("Cererea a fost efectuată cu succes!")
    
    # Răspunsul JSON
    response_data = response.json()
    print("Răspuns:", response_data)
    
    # Extracția access token-ului
    access_token = response_data.get('access')
    
    if access_token:
        print("Access Token:", access_token)
    else:
        print("Access Token-ul nu a fost găsit în răspuns.")
else:
    print("A apărut o eroare:", response.status_code, response.text)
