import requests

url = "https://api.peviitor.ro/v3/total/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print(f"Numărul de job-uri: {data['total']['jobs']}")
    print(f"Numărul de companii: {data['total']['companies']}")
else:
    print(f"Eroare la cererea API: {response.status_code}")
