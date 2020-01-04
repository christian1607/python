import requests

response = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
print(response.text)


#def call_ycombinator():
#    return requests.get("https://news.ycombinator.com/")
