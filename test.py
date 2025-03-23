import requests

TOKEN = "7987718226:AAHjF8XozKueiCWOj7p0250KMiyGNeB9tYY"
url = f"https://api.telegram.org/bot{TOKEN}/getMe"
response = requests.get(url)

print(response.json())  # Agar to'g'ri bo'lsa {"ok": true, ...} chiqadi
