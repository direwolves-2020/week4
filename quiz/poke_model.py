import requests
import sqlite3
#I needed to do this because my company's firewall was not cooperating with this request
import urllib3
urllib3.disable_warnings()


db = 'poke.db'
conn = sqlite3.connect(db)

class PokemonEntity:
    def __init__(self):
        self.pokedex_id = None
        self.name = None
        self.species_id = None
        self.user_pokemon_relation_id = None
        self.color = None
        self.habitat = None
        self.shape = None
    
    def __str__(self):
        return (self.name)


class UserEntity:
    def __init__(self):
        self.id = None
        self.name = None
        self.pokemon = []


class PokeDao:
    @staticmethod
    #This should get the user's id and name
    def fetch_user(username):
        user_entity = UserEntity()

        c = conn.cursor()
        c.execute(f"""
        SELECT * FROM user WHERE name = '{username}';
        """)
        user_info = c.fetchone()
        c.close()
        if user_info == None:
            return 'User not found'
        else:
            user_entity.id = user_info[0]
            user_entity.name = user_info[1]
            return user_entity
        
    #This is used after the member logs in, we fetch all of the pokemon that they own.
    @staticmethod
    def fetch_user_pokemon(user_id):
        poke_entity = PokemonEntity()
        user_entity = UserEntity()

        c = conn.cursor()
        c.execute(f"""
        SELECT pokemon.* , user_pokemon_link.id
        FROM pokemon, user_pokemon_link
        WHERE user_pokemon_link.user_id = {user_id}
        AND user_pokemon_link.pokemon_id = pokemon.id;
        """)
        poke_list = c.fetchall()

        #catches anyone who doesn't own any pokemon
        if len(poke_list) == 0:
            return []

        list_of_pokemon_entities = []
        #Looping through each pokemon and create a pokemon object to pass back to controller
        for pokemon in poke_list:
            poke_entity = PokemonEntity()

            #Creating poke_entity to pass back to controller
            poke_entity.pokedex_id = pokemon[0]
            poke_entity.name = pokemon[1]
            poke_entity.species_id = pokemon[2]
            poke_entity.user_pokemon_relation_id = pokemon[3]
            
            #Man, this is ugly. While in the for loop for each pokemon, I am grabbing the additional information from the 'pokemon_species' table to complete my poke_entity
            c.execute(f"""
            SELECT * from pokemon_species WHERE
            id = {pokemon[2]};
            """)
            poke_species_info = c.fetchall()
            poke_entity.habitat = poke_species_info[0][1]
            poke_entity.shape = poke_species_info[0][2]
            poke_entity.color = poke_species_info[0][3]
            list_of_pokemon_entities.append(poke_entity)
        user_entity.pokemon = list_of_pokemon_entities

        c.close()
        return user_entity.pokemon
        
        
    
    @staticmethod
    def add_user(new_username):
        user_entity = UserEntity()
        
        c = conn.cursor()
        c.execute(f"""
        INSERT INTO user (name)
        VALUES ('{new_username}');
        """)
        conn.commit()
        c.close()
        
        user_entity.id = c.lastrowid
        user_entity.name = new_username
        return user_entity

    #This is needed for both adding and deleting pokemon
    #Before adding or deleting anything, I need to perform a check to ensure the pokemon hasn't already been found in the wild and documented in the DB by another user
    @staticmethod
    def check_existence_of_pokemon_in_sql(pokemon_to_add):
        c = conn.cursor()
        c.execute(f"""        
            SELECT * FROM pokemon WHERE name = '{pokemon_to_add}';
            """)

        poke_info = c.fetchone()
        c.close()
        #IF it doesnt exist return False
        if poke_info == None:
            return False
        #Otherwise return True plus the existence variable (used for deleting)
        else:
            poke_entity = PokemonEntity()
            poke_entity.pokedex_id = poke_info[0]
            poke_entity.name = poke_info[1]
            poke_entity.species_id = poke_info[2]
            return (True, poke_entity)


    
    @staticmethod
    def add_existing_pokemon(new_pokemon_id, user_id):
        c = conn.cursor()
        inserting = c.execute(
        f"""
        INSERT INTO user_pokemon_link (user_id, pokemon_id)
        VALUES ('{user_id}', '{new_pokemon_id}');
        """
        )
        conn.commit()
        c.close()
        return PokeDao.fetch_user_pokemon(user_id)



    @staticmethod
    def add_new_pokemon(new_pokemon, user_id):
        #first searching for the pokemon
        r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{new_pokemon}/', verify = False)
        status_code = r.status_code
        if status_code == 200:
            poke_json = r.json()
            #This gets the link to the poke-species
            poke_species_id = poke_json['species']['url']
            #then going into poke-species to get additional info
            r = requests.get(poke_species_id, verify = False)
            poke_species_json = r.json()


            #Creating poke_entity to pass back to controller
            poke_entity = PokemonEntity()
            poke_entity.pokedex_id = poke_json['id']
            poke_entity.name = poke_json['name']
            poke_entity.species_id = poke_species_json['id']
            poke_entity.color = poke_species_json['color']['name']
            poke_entity.habitat = poke_species_json['habitat']['name']
            poke_entity.shape = poke_species_json['shape']['name']

            #Finally updating local DB
            c = conn.cursor()
            inserting = c.execute(
                f"""
                INSERT INTO pokemon (id, name, species_id)
                VALUES ('{poke_entity.pokedex_id}', '{poke_entity.name}', '{poke_entity.species_id}');
                """
            )
            conn.commit()


            inserting = c.execute(
                f"""
                INSERT INTO pokemon_species (id, habitat, shape, color)
                VALUES ('{poke_entity.species_id}', '{poke_entity.habitat}', '{poke_entity.shape}', '{poke_entity.color}');
                """
            )
            conn.commit()

            inserting = c.execute(
                f"""
                INSERT INTO user_pokemon_link (user_id, pokemon_id)
                VALUES ('{user_id}', '{poke_entity.pokedex_id}');
                """
            )
            conn.commit()
            poke_entity.user_pokemon_relation_id = c.lastrowid
            c.close()
            return poke_entity
        
        else:
            return 'Pokemon not found'

    
    #This deletes from the user_pokemon_link
    @staticmethod
    def delete_pokemon(id):
        c = conn.cursor()
        inserting = c.execute(
            f"""
            DELETE FROM user_pokemon_link 
            WHERE id = {id};
            """)
        conn.commit()
        c.close()



    #lookup all, lookup by species, lookup by habitat
    @staticmethod
    def lookup_by_habitat(habitat, user_id):
        c = conn.cursor()
        c.execute(f"""
            Select pokemon.name
            From pokemon
            INNER JOIN pokemon_species ON pokemon_species.id = pokemon.species_id
            INNER JOIN user_pokemon_link ON user_pokemon_link.pokemon_id = pokemon.id
            WHERE pokemon_species.habitat = '{habitat}' AND user_pokemon_link.user_id = {user_id};
            """)
        list_of_names = c.fetchall()
        return list_of_names

    def test():
        c = conn.cursor()
        c.execute("""
        Select pokemon.*, pokemon_species.habitat, pokemon_species.shape, pokemon_species.color
        From pokemon, pokemon_species
        INNER JOIN user_pokemon_link ON user_pokemon_link.pokemon_id = pokemon.id
        INNER JOIN pokemon_species ON pokemon_species.id = pokemon.species_id
        WHERE user_pokemon_link = 1 AND user_pokemon_link.pokemon_id = pokemon.id;
        """)
        list_of_pokemon = c.fetchall()
        return list_of_pokemon


PokeDao.test()
