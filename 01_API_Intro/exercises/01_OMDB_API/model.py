import requests
import sqlite3
#API key af94557e

#class to hold movies with only movie and year
class Movie_brief: 
    #value is how user will select individual movie
    def __init__(self, movie, year, value):
        self.movie = movie
        self.year = year
        self.value = value

    #Converting movie object into a string
    def __str__(self):
        return f"{self.value} - Title: {self.movie} \n    Release Year: {self.year} \n\n"

class Movie_full: 

    def __init__(self, title, year, director, actors, plot, rating): 
        self.title = title
        self.year = year
        self.director = director
        self.actors = []

class DAO:

    key = "af94557e"

    @staticmethod
    def get_request(title):

        payload = {
            "apikey": f"{DAO.key}",
            "s": f"{title}"
        }

        response = requests.get("http://omdbapi.com/", params=payload)
        response_json = response.json()
        return response_json

    #takes search query and builds a list of results    
    @staticmethod
    def show_results(search_results): 

        print("\n")
        value = 1
        result_lst = []
        for result in search_results["Search"]: 
            movie = Movie_brief(result["Title"], result["Year"], value)
            value += 1
            result_lst.append(movie)
            print(movie)

        return result_lst

    #returns specific movie from list that client selects
    @staticmethod
    def show_selection(selection, lst): 
        selection_int = int(selection)
        if selection_int <= len(lst) and selection_int > 0: 
            print("\n" + str(lst[selection_int - 1]))
            return lst[selection_int - 1]
        else: 
            print("You selected a number that was not on the list!")

    @staticmethod
    def specific_search(input): 

        payload = {
            "apikey": f"{DAO.key}",
            "t": str(input.movie)
        }

        response = requests.get("http://omdbapi.com/", params=payload)
        response_json = response.json()
        for actors in response_json["Actors"]: 
            actor_lst = []
            actor_lst.append(actors["Actors"])
        for i in actor_lst: 
            print(i)


        return response_json





