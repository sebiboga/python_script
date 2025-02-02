import requests

# URL-ul endpoint-ului API
url = "http://peviitorqa.go.ro/api/v0/companies/"

# Funcția pentru a obține companiile
def get_companies():
    # Adăugăm un antet User-Agent
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    # Facem cererea GET la API
    response = requests.get(url, headers=headers)

    # Verificăm dacă cererea a avut succes
    if response.status_code == 200:
        data = response.json()
        
        # Extragem lista de companii
        companies = data.get("companies", [])
        
        # Afișăm numele companiilor
        if companies:
            print("Companii găsite:")
            for company in companies:
                print(f"- {company['name']}")
        else:
            print("Nu s-au găsit companii.")
    else:
        print(f"Eroare la cererea API: {response.status_code}")

# Apelăm funcția direct
get_companies()
