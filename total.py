import requests

# URL-ul endpoint-ului API
url = "https://api.peviitor.ro/v3/total/"

# Facem cererea GET la API
response = requests.get(url)

# Verificăm dacă cererea a avut succes
if response.status_code == 200:
    # Decodăm JSON-ul
    data = response.json()
    
    # Extragem numărul de job-uri și numărul de companii
    num_jobs = data['total']['jobs']
    num_companies = data['total']['companies']
    
    # Tipărim rezultatele
    print(f'Numărul de job-uri: {num_jobs}')
    print(f'Numărul de companii: {num_companies}')
else:
    print(f'Eroare la cererea API: {response.status_code}')
