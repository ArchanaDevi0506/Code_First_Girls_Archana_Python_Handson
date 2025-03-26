import requests
response = requests.get("https://api.github.com/users/defunkt")
print(response.json())
print(response.status_code)


