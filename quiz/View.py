from Model import ModelDAO

class View:

    @staticmethod
    def restart():
        #ensures that the app runs continously
        choice = input("\nType 0 for more options. ")
        return choice
    

    @staticmethod
    def enter_username():
        username = input("\nEnter a username to log in or create an account: ")
        return str(username)

    
    @staticmethod
    def invalid_username():
        print("Username must be longer than two characters. ")


    @staticmethod
    def welcome_user(user):
        print("Welcome", str(user).title(), '\n')


    @staticmethod
    def get_password():
        password = input("Please enter your password: ")
        return password
    

    @staticmethod
    def incorrect_password():
        print("Incorrect password.")


    @staticmethod
    def add_user():
        password = input("No user found. Please enter a password to create an account: ")
        return password


    @staticmethod
    def show_home_screen():
        choice = input(
        """
        What would you like to do? 
            1 - Add a pokemon
            2 - Delete a pokemon
            3 - View your pokemons
            4 - View your pokemons by species
            5 - View your pokemons by habitat \n
        """)
        return choice


    @staticmethod
    def show_pokemon(names):
        print("\nHere is the list of pokemons to choose from: ", *names, sep='\n')


    @staticmethod
    def add_pokemon():
        pokemon_to_add = input("\nPlease enter pokemon to add: ")
        return pokemon_to_add
    

    @staticmethod
    def show_added_pokemon(added_pokemon):
        print("Added", added_pokemon)


    @staticmethod
    def delete_pokemon():
        pokemon_to_delete = input("Please enter the id of the entry to delete: ")
        return pokemon_to_delete

    
    @staticmethod
    def view_all_pokemon(num):
        print("\nYou have", num, "pokemons: ")

    @staticmethod
    def show_column_names():
        print("ID, Username, Pokemon ID, Pokemon Name, Species, Habitat")


    @staticmethod
    def view_all_pokemon_by_species():
        species_to_view = input("\nEnter the species to search by: ")
        return species_to_view
      
    
    @staticmethod
    def view_all_pokemon_by_habitat():
        habitat_to_view = input("\nEnter the habitat to search by: ")
        return habitat_to_view     