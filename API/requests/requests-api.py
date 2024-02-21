import requests
import json

r = requests.get("https://randomuser.me/api/")
print(r.status_code)
print("\n")
print(r.text)
print("\n")
print(r.encoding)
print("\n")
print(r.json()["results"][0]["gender"])
print("\n")
print(r.json()["results"][0]["name"]["first"])
print("\n")
print(r.json()["results"][0]["location"]["city"])