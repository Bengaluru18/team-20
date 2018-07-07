import requests

base_url = "http://localhost:8080"
print "hi"
url = base_url  #TODO
params = { "pid" : "20170404", "sid" : "54678234"}
response = requests.get ( url, params = params)

print response.text