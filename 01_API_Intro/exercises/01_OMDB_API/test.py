import requests 
key = "af94557e"
r = requests.get("http://www.omdbapi.com/?apikey=af94557e&s=Dodgeball")


response = print(r.json())
