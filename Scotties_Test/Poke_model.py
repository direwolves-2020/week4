import requests
import sqlite3



class User: 

    def __init__(self, username, password):
        self.username = username
        self.password = password 

class Pokemon: 

    def __init__(self, name, habitat, types = [None, None]):
        self.name = name 
        self.habitat = habitat 
        self.types = types 



class DAO:


    @staticmethod
    def create_user(User): 
        conn = sqlite3.connect("Pokemon")
        c = conn.cursor()
        c.execute("""
            INSERT INTO USERS ("username", "password") 
            VALUES (?,?)""", (User.username, User.password))
        conn.commit()
        c.close()
        conn.close()

    #this is how I authenticate a user, let me know if theres a better way
    #read that try/excepts may be ineffecient but it was the best way
    #I could think of to handle errors and not kill the program
    @staticmethod
    def check_login(User): 
        try:
            conn = sqlite3.connect("Pokemon")
            c = conn.cursor()
            login = c.execute(
                f"""
                SELECT * FROM USERS 
                Where username = "{User.username}";
                """
            )
            info = login.fetchone()
            if info[1] == User.username and info[2] == User.password: 
                print(f"\nYou are logged in as {User.username}!")
                return True
            else: 
                print("\nThe Username or Password you entered is incorrect.")
                return False
        except TypeError: 
             print("\nThere was an error, please try again.")
             return False
        except sqlite3.Error as error:
            print("\nThere was an error, please try again.", error)
            return False
        finally:
            c.close()
            conn.close()


    #this function grabs a pokemons information based on name and puts it into .json
    #not sure if .json is even needed since the site delivers a json
    @staticmethod
    def get_pokemon_name(pokemon):
        #Had to concatenate as a ? would mess up search, any uppercase throws it off too
        response = requests.get("http://pokeapi.co/api/v2/pokemon/" + pokemon.lower() )
        #Checking to make sure there is no error in the response code
        if response.ok == True:
            response_json = response.json()
            return response_json
        else: 
            return False

    @staticmethod
    def get_pokemon_habitat(habitat):
        #Had to concatenate as a ? would mess up search, any uppercase throws it off too
        response = requests.get("http://pokeapi.co/api/v2/pokemon-habitat/" + habitat.lower() )
        #Checking to make sure there is no error in the response code
        if response.ok == True:
            response_json = response.json()
            return response_json
        else: 
            return False

    @staticmethod
    def get_type(types):
        #Had to concatenate as a ? would mess up search, any uppercase throws it off too
        response = requests.get("http://pokeapi.co/api/v2/type/" + types.lower() )
        #Checking to make sure there is no error in the response code
        if response.ok == True:
            response_json = response.json()
            return response_json
        else: 
            return False

    #this function takes the json from above and extracts the name, habitat and type info out
    #if the user confirms the choice then it builds a new Pokemon instance with extracted data
    @staticmethod 
    def show_pokemon(pokemon): 

        print("\n")

        new_pokemon_name = pokemon["name"]

        new_pokemon_types = [None, None]
        index = 0
        for types in pokemon["types"]:
            p_type = types["type"]["name"]
            new_pokemon_types[index] = p_type
            index += 1

        species_url = pokemon["species"]["url"]
        #see comment below
        habitat = DAO.get_habitat(species_url)


        print("Name: " + new_pokemon_name)
        count = 1
        for types in new_pokemon_types: 
            if types:
                print("Type " + str(count) + ": " + types)
                count += 1
        print("Habitat: " + habitat)

        new_pokemon = Pokemon(new_pokemon_name, habitat, new_pokemon_types)
        return new_pokemon
    
    #habitat info was not in /pokemon endpoint but it was in /pokemon-speices
    #the api endpoint for the queried pokemon-species query is in /pokemon response
    #have to hit this and return extracted habitat information to show_pokemon
    @staticmethod
    def get_habitat(url):
        response = requests.get(url)
        response_json = response.json()
        habitat = response_json["habitat"]["name"]
        return habitat


    #This shows all of the CURRENT USERS pokemon that they have added
    @staticmethod
    def view_pokemon(user):
        conn = sqlite3.connect("Pokemon")
        c = conn.cursor()

        user_query = c.execute("SELECT * FROM USERS WHERE (username=?)", (user.username,))
        user_info = user_query.fetchone()
        user_id = user_info[0]

        #this is the query I had the most trouble with, I could not get the desired output 
        #included in the comment I had on Create_and_seed file line 73
        #had to refactor database to have to type_ids in POKEMON_TYPES
        #then had issues returning pokemon with only one type as type_id_2 would be null
        #solved this with a LEFT OUTER JOIN for that join on and set the type to return to "None" if it was null
        user_pokemon = c.execute(
        """
        SELECT Pokemon.name, Pokemon.habitat, t1.type, ifnull(t2.type, "None")
                       FROM POKEMON
                       INNER JOIN POKEMON_TYPES
                       ON POKEMON.id = POKEMON_TYPES.pokemon_id
                       INNER JOIN TYPES t1
                       ON POKEMON_TYPES.type_id = t1.id
                       LEFT OUTER JOIN TYPES t2
                       ON POKEMON_TYPES.type_id_2 = t2.id
                       INNER JOIN USERS_POKEMON
                       ON POKEMON.id = USERS_POKEMON.pokemon_id
                       WHERE (USERS_POKEMON.user_id = ?)
      """,(user_id,))

        full_list = user_pokemon.fetchall()
        #inserting headers to position 0
        headers = ["POKEMON", "HABITAT", "TYPE 1", "TYPE 2"]
        full_list.insert(0, headers)

        c.close()
        conn.close()

        return full_list
     
       
      

    @staticmethod
    def view_pokemon_by_type(user, types): 
        conn = sqlite3.connect("Pokemon")
        c = conn.cursor()


        user_query = c.execute("SELECT * FROM USERS WHERE (username=?)", (user.username,))
        user_info = user_query.fetchone()
        user_id = user_info[0]

    
        user_pokemon = c.execute(
        """SELECT Pokemon.name, Pokemon.habitat, t1.type, ifnull(t2.type, "None")
                       FROM POKEMON
                       INNER JOIN POKEMON_TYPES
                       ON POKEMON.id = POKEMON_TYPES.pokemon_id
                       INNER JOIN TYPES t1
                       ON POKEMON_TYPES.type_id = t1.id
                       LEFT OUTER JOIN TYPES t2
                       ON POKEMON_TYPES.type_id_2 = t2.id
                       INNER JOIN USERS_POKEMON
                       ON POKEMON.id = USERS_POKEMON.pokemon_id
                       WHERE USERS_POKEMON.user_id = ? AND (t1.type = ? OR t2.type =?)""",(user_id, types, types))
        full_list = user_pokemon.fetchall()
        headers = ["POKEMON", "HABITAT", "TYPE 1", "TYPE 2"]
        full_list.insert(0, headers)
        
        c.close()
        conn.close()
        if len(full_list) > 1:
            return full_list
        else: 
            print("You have no Pokemon of that type!")
            return False

    @staticmethod
    def view_pokemon_by_habitat(user, habitat): 
        conn = sqlite3.connect("Pokemon")
        c = conn.cursor()


        user_query = c.execute("SELECT * FROM USERS WHERE (username=?)", (user.username,))
        user_info = user_query.fetchone()
        user_id = user_info[0]

    
        user_pokemon = c.execute(
        """SELECT Pokemon.name, Pokemon.habitat, t1.type, ifnull(t2.type, "None")
                       FROM POKEMON
                       INNER JOIN POKEMON_TYPES
                       ON POKEMON.id = POKEMON_TYPES.pokemon_id
                       INNER JOIN TYPES t1
                       ON POKEMON_TYPES.type_id = t1.id
                       LEFT OUTER JOIN TYPES t2
                       ON POKEMON_TYPES.type_id_2 = t2.id
                       INNER JOIN USERS_POKEMON
                       ON POKEMON.id = USERS_POKEMON.pokemon_id
                       WHERE USERS_POKEMON.user_id = ? AND POKEMON.habitat = ?""",(user_id, habitat))
        full_list = user_pokemon.fetchall()
        headers = ["POKEMON", "HABITAT", "TYPE 1", "TYPE 2"]
        full_list.insert(0, headers)
        c.close()
        conn.close()

        if len(full_list) > 1:
            return full_list
        else: 
            print("You have no Pokemon of that type!")
            return False
    @staticmethod
    def delete_pokemon(pokemon, user):
        conn = sqlite3.connect("Pokemon")
        c = conn.cursor()

        pokemon_query = c.execute("SELECT * FROM POKEMON WHERE (name=?)", (pokemon.name,))
        pokemon_info = pokemon_query.fetchone()
        pokemon_id = pokemon_info[0]

        user_query = c.execute("SELECT * FROM USERS WHERE (username=?)", (user.username,))
        user_info = user_query.fetchone()
        user_id = user_info[0]

        c.execute("DELETE FROM USERS_POKEMON WHERE (user_id=? AND pokemon_id=?)", (user_id, pokemon_id) )
        print("This pokemon is no longer on your account!")
        conn.commit()
        c.close()
        conn.close()    


    @staticmethod
    def create_pokemon(pokemon, user): 
        DAO.insert_pokemon_table(pokemon, user)
        DAO.insert_types_table(pokemon, user)
        DAO.insert_pokemon_types_table(pokemon, user)
        DAO.insert_users_pokemon_table(pokemon, user)

    @staticmethod 
    def insert_pokemon_table(pokemon, user):
        conn = sqlite3.connect("Pokemon")
        c = conn.cursor()
        pokemon_entry = c.execute("SELECT * FROM POKEMON WHERE (name=? AND habitat=?)", (pokemon.name, pokemon.habitat))
        entry = pokemon_entry.fetchone()

        if entry is None:
            c.execute("""
                INSERT INTO POKEMON ("name", "habitat") 
                VALUES (?,?)""", (pokemon.name, pokemon.habitat))
            print("New Pokemon added")
        else:
            print("Pokemon exists")

        conn.commit()
        c.close()
        conn.close()       

    #Adding to TYPES Table
    @staticmethod
    def insert_types_table(pokemon, user):
        conn = sqlite3.connect("Pokemon")
        c = conn.cursor()
        for types in pokemon.types:
           
            type_entry = c.execute("SELECT * FROM TYPES WHERE type=?", (types,))
            types_entry = type_entry.fetchone()

            if types_entry is None and types:
                c.execute("""
                    INSERT INTO TYPES ("type") 
                    VALUES (?)""", (types,))
                print("New Type added")
            else:
                print("Type exists") 
            conn.commit()

        c.close()
        conn.close()

    @staticmethod
    def insert_pokemon_types_table(pokemon, user):
        conn = sqlite3.connect("Pokemon")
        c = conn.cursor()
        #finding the pokemon id that we just inserted
        find_pokemon_id = c.execute("SELECT * FROM POKEMON WHERE (name=? AND habitat=?)", (pokemon.name, pokemon.habitat))
        pokemon_id_result = find_pokemon_id.fetchone()
        p_id = pokemon_id_result[0]
        #finding the type id we just inserted
        
        find_type_id = c.execute("SELECT * FROM TYPES WHERE type=?", (pokemon.types[0],))
        type_id_result = find_type_id.fetchone()
        t_id = type_id_result[0]
        if pokemon.types[1]:
            find_type_id = c.execute("SELECT * FROM TYPES WHERE type=?", (pokemon.types[1],))
            type_id_result = find_type_id.fetchone()
            t_id_2 = type_id_result[0]
        else: 
            t_id_2 = "Null"

        pokemon_types_entry = c.execute("SELECT * FROM POKEMON_TYPES WHERE (pokemon_id=? AND type_id=? AND type_id_2=?)", (p_id, t_id, t_id_2))
        entry = pokemon_types_entry.fetchone()

        if entry is None:
            c.execute("""
                INSERT INTO POKEMON_TYPES ("pokemon_id", "type_id", "type_id_2") 
                VALUES (?,?,?)""", (p_id, t_id, t_id_2))
            print("New Pokemon Types entry added")
        else:
            print("Pokemon Types entry exists")

        conn.commit()
        c.close()
        conn.close()

    @staticmethod
    def insert_users_pokemon_table(pokemon, user):

        conn = sqlite3.connect("Pokemon")
        c = conn.cursor()

        find_pokemon_id = c.execute("SELECT * FROM POKEMON WHERE (name=? AND habitat=?)", (pokemon.name, pokemon.habitat))
        pokemon_id_result = find_pokemon_id.fetchone()
        p_id = pokemon_id_result[0]

        #Adding Pokemon to USERS_POKEMON TABLE
        find_user_id = c.execute("SELECT * FROM USERS WHERE username=? AND password=?", (user.username, user.password))
        user_id_result = find_user_id.fetchone()
        user_id = user_id_result[0]


        users_pokemon_entry = c.execute("SELECT * FROM USERS_POKEMON WHERE (user_id=? AND pokemon_id=?)", (user_id, p_id))
        entry = users_pokemon_entry.fetchone()

        if entry is None:
            c.execute("""
                INSERT INTO USERS_POKEMON ("user_id", "pokemon_id") 
                VALUES (?,?)""", (user_id, p_id))
            print(f"New Pokemon added to {user.username}'s account!'")
        else:
            print("You already have this pokemon!")

        conn.commit()



        c.close()
        conn.close()    

       


