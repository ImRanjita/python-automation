import requests

url = "https://api.languagetoolplus.com/v2/check"

data = {
    "text": "This is a nixe day",
    "language": "en"
}
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, data=data)
print(response.text)
