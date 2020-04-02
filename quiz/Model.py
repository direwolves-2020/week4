import requests
import sqlite3

class User:
    def __init__(self, username):
        self.username = username
        self.password = None
    
    def __str__(self):
        return str(self.username)


class Pokemon:
    def __init__(self):
        self.pokemon_id = None
        self.pokemon_name = None
        self.species_name = None
        self.habitat_name = None
    
    def __str__(self):
        return str(self.pokemon_name)


class Species:
    def __init__(self):
        self.species_name = None
    
    def __str__(self):
        return str(self.species_name)


class Habitat:
    def __init__(self):
        self.habitat_name = None


class ModelDAO:

    @staticmethod
    def add_user(username, password):
        #adds a user into the user table
        conn = sqlite3.connect('pokemon_database.db')
        c = conn.cursor()
        
        c.execute(
            f""" INSERT INTO user (username, password)
                VALUES ("{username}", "{password}");
            """    
        )
        conn.commit()
        c.close()
 
 
    @staticmethod
    def get_user(username):
        #gets all user pokemons
        conn = sqlite3.connect('pokemon_database.db')
        c = conn.cursor()
        
        result = c.execute(
            f""" SELECT * FROM user
            WHERE username = "{username}";   
            """  
        )
        rows = [item[0] for item in result.fetchall()]
        return rows


    @staticmethod
    def get_all_users():
        #gets all users
        conn = sqlite3.connect('pokemon_database.db')
        c = conn.cursor()
        
        result = c.execute(
            f""" SELECT username FROM user;
            """  
        )
        return result.fetchall()


    def get_password(username, password):
        #gets user's password
        conn = sqlite3.connect('pokemon_database.db')
        c = conn.cursor()
        
        result = c.execute(
            f""" SELECT * FROM user
            WHERE username = "{username}"
            AND password = "{password}";   
            """  
        )
        return result.fetchall()


    @staticmethod
    def add_pokemon(pokemon_id, username): 
        #adds a pokemon for a specific user
        conn = sqlite3.connect('pokemon_database.db')
        c = conn.cursor()
        
        c.execute(
            f""" INSERT INTO user_pokemon (pokemon_id, username) 
                VALUES ("{pokemon_id}", "{username}");
            """    
        )
        conn.commit()
        c.close()


    @staticmethod
    def delete_pokemon(id, username):
        #deletes a pokemon for a specific user
        conn = sqlite3.connect('pokemon_database.db')
        c = conn.cursor()
        
        c.execute(
            f""" DELETE FROM user_pokemon 
            WHERE id = "{id}"
            AND username = "{username}";
            """    
        )

        conn.commit()
        c.close()


    @staticmethod
    def view_all_user_pokemon(username):
        #gets all user's pokemons
        conn = sqlite3.connect('pokemon_database.db')
        c = conn.cursor()

        result = c.execute(
            f""" SELECT user_pokemon.id, user_pokemon.username, pokemon.*
                FROM pokemon, user_pokemon
                WHERE user_pokemon.username = "{username}"
                AND pokemon.pokemon_id = user_pokemon.pokemon_id;
            """
        )

        return result.fetchall()


    @staticmethod
    def view_all_pokemon_by_species(username, species):
        #gets all user's pokemons by species
        conn = sqlite3.connect('pokemon_database.db')
        c = conn.cursor()

        c.execute(
            f"""SELECT user_pokemon.id, user_pokemon.username, pokemon.*
                FROM pokemon, user_pokemon, species
                WHERE user_pokemon.username = "{username}"
                AND pokemon.pokemon_id = user_pokemon.pokemon_id
                AND species.species_name = "{species}"
                AND pokemon.species_name = species.species_name;
            """ 
        )
        result = c.fetchall()
        c.close()
        return result


    @staticmethod
    def view_all_pokemon_by_habitat(username, habitat):
        #gets all user's pokemons by habitat
        conn = sqlite3.connect('pokemon_database.db')
        c = conn.cursor()

        c.execute(
            f"""SELECT user_pokemon.id, user_pokemon.username, pokemon.*
                FROM pokemon, user_pokemon, habitat
                WHERE user_pokemon.username = "{username}"
                AND pokemon.pokemon_id = user_pokemon.pokemon_id
                AND habitat.habitat_name = "{habitat}"
                AND pokemon.habitat_name = habitat.habitat_name;
            """ 
        )
        result = c.fetchall()
        c.close()
        return result


    @staticmethod
    def seed_pokemon(names):
       
        #get API
        response = requests.get(f"http://pokeapi.co/api/v2/pokemon-species/{names}")
        json_response = response.json()
             
        if response.status_code != 200:
            print("Not found")
        else:
            #create Pokemon objects
            pokemon = Pokemon()
            pokemon.pokemon_id = json_response['id']
            pokemon.pokemon_name = json_response['name']
            pokemon.species_name = json_response['name']
            pokemon.habitat_name = json_response['habitat']['name']

            results = []
            results.append(pokemon)

        #insert into db
        conn = sqlite3.connect('pokemon_database.db')
        c = conn.cursor()
        
        #c.execute(""" DELETE FROM pokemon """)

        result = c.execute(
            f""" INSERT INTO pokemon (pokemon_id, pokemon_name, species_name, habitat_name)
                VALUES ("{pokemon.pokemon_id}", "{pokemon.pokemon_name}", "{pokemon.species_name}", "{pokemon.habitat_name}");   
            """  
        )
        
        conn.commit()
        c.close()


    @staticmethod
    def get_pokemon_table():
        #gets everything in the pokemon table
        conn = sqlite3.connect('pokemon_database.db')
        c = conn.cursor()
        
        result = c.execute(
            f""" SELECT * FROM pokemon; """  
        )
        return result.fetchall()


    @staticmethod
    def seed_species(names):
       
        #get API
        response = requests.get(f"http://pokeapi.co/api/v2/pokemon-species/{names}")
        json_response = response.json()
             
        if response.status_code != 200:
            print("Not found")
        else:
            #create Species objects
            species = Species()
            species.species_name = json_response['name']

            results = []
            results.append(s)

        #insert into db
        conn = sqlite3.connect('pokemon_database.db')
        c = conn.cursor()
        
        # c.execute(""" DELETE FROM species """)

        result = c.execute(
            f""" INSERT INTO species (species_name)
                VALUES ("{species.species_name}");   
            """  
        )
        
        conn.commit()
        c.close()


    @staticmethod
    def get_species_table():
        #gets everything in the species table
        conn = sqlite3.connect('pokemon_database.db')
        c = conn.cursor()
        
        result = c.execute(
            f""" SELECT * FROM species; """  
        )
        return result.fetchall()


    @staticmethod
    def seed_habitat(habitat_names):

        #get API
        response = requests.get(f"http://pokeapi.co/api/v2/pokemon-habitat/{habitat_names}")
        json_response = response.json()
             
        if response.status_code != 200:
            print("Not found")
        else:
            #create Habitat objects
            habitat = Habitat()
            habitat.habitat_name = json_response['name']

            results = []
            results.append(s)

        #insert into db
        conn = sqlite3.connect('pokemon_database.db')
        c = conn.cursor()
        
        # c.execute(""" DELETE FROM habitat """)

        result = c.execute(
            f""" INSERT INTO habitat (habitat_name)
                VALUES ("{habitat.habitat_name}");   
            """  
        )
        
        conn.commit()
        c.close()


    @staticmethod
    def get_habitat_table():
        #gets everything in the habitat table
        conn = sqlite3.connect('pokemon_database.db')
        c = conn.cursor()
        
        result = c.execute(
            f""" SELECT * FROM habitat;   
            """  
        )
        # rows = [item[0] for item in result.fetchall()]
        return result.fetchall()


   
class PokeAPI:

    @staticmethod
    def get_all_pokemon():
        #gets a list of pokemons from the API
        response = requests.get("http://pokeapi.co/api/v2/pokemon/")
        json_response = response.json()
             
        if response.status_code != 200:
            print("Not found")
        else:
            search_results = json_response["results"]
            
            results = []
            for result in search_results:
                pokemon = Pokemon()
                pokemon.pokemon_name = result['name']
                results.append(pokemon.pokemon_name)
           
        return results


    @staticmethod
    def get_all_habitats():
        #gets a list of habitats from the API
        response = requests.get("http://pokeapi.co/api/v2/pokemon-habitat/")
        json_response = response.json()
             
        if response.status_code != 200:
            print("Not found")
        else:
            search_results = json_response["results"]
            
            results = []
            for result in search_results:
                habitat = Habitat()
                habitat.habitat_name = result['name']
                results.append(habitat.habitat_name)
           
        return results


    @staticmethod
    def get_pokemon_id(pokemon_name):
        #gets the pokemon id for each pokemon
        response = requests.get(f"http://pokeapi.co/api/v2/pokemon/{pokemon_name}")
        json_response = response.json()
        
        if response.status_code != 200:
            print("Not found")
        else:
            p = Pokemon()
            p.pokemon_name = json_response["name"]
            p.pokemon_id = json_response['id']
            p.species_name = json_response['species']['name']

        return p.pokemon_id


