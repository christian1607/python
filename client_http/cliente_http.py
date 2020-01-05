import requests
import pyfiglet

print(pyfiglet.figlet_format("JOKE IS FUNNY"))

response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
print(response.text)

data = response.json()
print(f'A Joke: {data["joke"]}')

# def call_ycombinator():
#    return requests.get("https://news.ycombinator.com/")

# Query param
term = input("Type a joke term: ")
search_response = requests.get("https://icanhazdadjoke.com/search",
                               headers={"Accept": "application/json"},
                               params={
                                   "term": term
                               })

data_search = search_response.json()
for index in range(len(data_search["results"])):
    print(f'{ index+1 , data_search["results"][index]["joke"]}')
