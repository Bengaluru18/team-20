import requests

base_url = "http://localhost:5000"

url = base_url + "/api/hello" #TODO
params = { "name" : "Aravind", "num" : "1053"}
response = requests.get ( url, params = params)

print response.text