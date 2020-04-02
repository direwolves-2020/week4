from Model import ModelDAO, PokeAPI, Pokemon, User, Species, Habitat
from View import View

class Controller:

    #global variable to hold current user
    user_name = View.enter_username()
    current_user = User(user_name)


    def __init__(self):
        view = View()
        model = ModelDAO()
        poke = PokeAPI()
        user = User(self.current_user)
        pokemon = Pokemon()
        species = Species()
        habitat = Habitat()


    def start(self):
        self.check_user()
        self.view_home_screen()


    def restart(self):
        choice = View.restart()
        if choice == "0":
            c.view_home_screen()
        self.restart()


    def view_home_screen(self):
        choice = View.show_home_screen()
        if int(choice) == 1:
            self.add_pokemon()
        elif int(choice) == 2:
            self.delete_pokemon()        
        elif int(choice) == 3:
            self.view_all_user_pokemon()
        elif int(choice) == 4:
            self.view_all_pokemon_by_species()    
        elif int(choice) == 5:
            self.view_all_pokemon_by_habitat()
        else:
            self.view_home_screen() 
    

    def check_user(self):
        #ensures that username is greater than 2 characters
        if len(str(self.current_user)) < 3:
            View.invalid_username()
            self.current_user = View.enter_username()
            self.check_user()
        else:
            self.login_or_add_user()


    def login_or_add_user(self):
        #username exists
        if ModelDAO.get_user(self.current_user):
            password = View.get_password()

            #password is correct
            if ModelDAO.get_password(self.current_user, password):
                View.welcome_user(self.current_user)

            #password is incorrect
            else:
                View.incorrect_password()
                password = View.get_password()

                if ModelDAO.get_password(self.current_user, password):
                    View.welcome_user(self.current_user)
                else:
                    self.get_password_attempts()
                    self.login_or_add_user()     

        #username doesn't exist
        else:
            password = View.add_user()
            ModelDAO.add_user(self.current_user, password)
            View.welcome_user(self.current_user)


    def get_password_attempts(self):
        #limits password attempts
        count = 2 
        while count < 3:
            password = View.get_password()
            count += 1
        print("Too many attempts. ")


    def add_pokemon(self):
        #gets the list of pokemons from the API
        pokemon_list = PokeAPI.get_all_pokemon()
        View.show_pokemon(pokemon_list)

        #create a pokemon object 
        pokemon_to_add = View.add_pokemon()
        if pokemon_to_add not in pokemon_list:
            print(pokemon_to_add, "is not a valid pokemon to add. ")
            self.add_pokemon()
        else:
            #adds the pokemon to the logged in user
            p = Pokemon()
            p.pokemon_name = pokemon_to_add
            p.pokemon_id = PokeAPI.get_pokemon_id(p.pokemon_name)
            ModelDAO.add_pokemon(p.pokemon_id, self.current_user)
            View.show_added_pokemon(p.pokemon_name)    


    def delete_pokemon(self):
        #deletes a pokemon from the user
        self.view_all_user_pokemon()
        id_to_delete = View.delete_pokemon()
        ModelDAO.delete_pokemon(id_to_delete, self.current_user)


    def view_all_user_pokemon(self):
        #shows all the user's pokemon 
        num = len(ModelDAO.view_all_user_pokemon(self.current_user))
        View.view_all_pokemon(num)
        all_pokemon = ModelDAO.view_all_user_pokemon(self.current_user)
        if num > 0: 
            View.show_column_names()
            print(*all_pokemon, sep='\n')


    def view_all_pokemon_by_species(self):
        #shows all the user's pokemon by species
        species_to_search = View.view_all_pokemon_by_species()
        pokemon_by_species = ModelDAO.view_all_pokemon_by_species(self.current_user, species_to_search)
        View.show_column_names()
        print(*pokemon_by_species, sep='\n')


    def view_all_pokemon_by_habitat(self):
        #shows all the user's pokemon by habitat
        habitat_to_seach = View.view_all_pokemon_by_habitat()
        pokemon_by_habitat = ModelDAO.view_all_pokemon_by_habitat(self.current_user, habitat_to_seach)
        View.show_column_names()
        print(*pokemon_by_habitat, sep='\n')


    def get_all_users(self):
        print(ModelDAO.get_all_users())


    def get_pokemon_habitats(self):
        print(*ModelDAO.get_habitat_table(), sep='\n')


    def get_pokemon_table(self):
        print(*ModelDAO.get_pokemon_table(), sep='\n')



if __name__ == "__main__":
    c = Controller()
    c.start()
    c.restart()
    
