import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()

print("\nTitle:")
print(data["title"])

print("\nBody:")
print(data["body"])