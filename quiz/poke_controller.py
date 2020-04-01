from poke_model import PokeDao
from poke_model import UserEntity
from poke_view import PokeView


class PokeController:
    def __init__(self, run_app=True):
        self.user = UserEntity()
        self.view = PokeView()
        if run_app:
            self.home_screen()

    def home_screen(self):
        user_input = self.view.home_screen_view()
        if user_input == '1':
            self.login_screen()
        elif user_input == '2':
            self.create_user()

    def create_user(self):
        new_user = self.view.new_user_view()
        new_user_entity = PokeDao.add_user(new_user)
        self.user = new_user_entity
        self.poke_portal()


    def login_screen(self):    
        username = self.view.login_screen_view()
        self.user = PokeDao.fetch_user(username)
        #If user does not exist, show error.. this isn't set up 100% properly. but overlooking because it's not pertinent to the purpose of the assignment
        if type(self.user) == str:
            self.view.login_error_view(self.user)
        #Else go get the pokemon associated with the user
        else:
            self.user.pokemon = PokeDao.fetch_user_pokemon(self.user.id)
            self.poke_portal()
    
    def poke_portal(self):
        user_action = self.view.poke_portal_view()
        if user_action == '1':
            self.view_user_pokemon()
        elif user_action == '2':
            self.add_pokemon_first_step()
        elif user_action == '3':
            self.delete_pokemon()
        elif user_action == '4':
            return print('Tchau!')

    def add_pokemon_first_step(self):
        #First get name of pokemon from user
        pokemon_to_add = self.view.add_pokemon_view()
        #Then check if the pokemon has already been documented by another user in the db
        existence = PokeDao.check_existence_of_pokemon_in_sql(pokemon_to_add)
        #If it doesn't exist, fetch from poke api
        if existence == False:
            self.add_undiscovered_pokemon(pokemon_to_add)
        #Else it does exist, go to the sql command instead
        else:
            self.add_pre_existing_pokemon(existence[1])

    #undiscovered pokemon need to be fetched out of the pokeAPI
    def add_undiscovered_pokemon(self,new_pokemon):
        new_pokemon = PokeDao.add_new_pokemon(new_pokemon, self.user.id)
        #string type means the pokemon wasn't found with the api call
        if type(new_pokemon) == str:
            self.view.pokemon_add_del_error_view()
        else:
            self.user.pokemon.append(new_pokemon)
            self.view.add_success_view()
        self.poke_portal()

    def add_pre_existing_pokemon(self, new_pokemon):
        #adding to the relation table
        new_list_of_pokemon = PokeDao.add_existing_pokemon(new_pokemon.pokedex_id, self.user.id)
        #add to user entity
        self.user.pokemon = new_list_of_pokemon
        self.view.add_success_view()
        self.poke_portal()

    def delete_pokemon(self):
        #First check if they have any pokemon
        if len(self.user.pokemon) == 0 :
            self.view.user_has_no_pokemon_view()
        else:
            pokemon_to_delete = self.view.delete_pokemon_view(self.user.pokemon)
            #get the user_relation unique link of the particular pokemon to be deleted
            deleting_id = self.user.pokemon[pokemon_to_delete].user_pokemon_relation_id
            #Delete from db
            PokeDao.delete_pokemon(deleting_id)
            #delete from user entity
            self.user.pokemon.remove(self.user.pokemon[pokemon_to_delete])
            self.view.delete_succes_view()
        self.poke_portal()


    def view_user_pokemon(self):
        #first need to check if this user has ANY pokemon
        if len(self.user.pokemon) == 0:
            self.view.user_has_no_pokemon_view()
            self.poke_portal
        
        user_action = self.view.view_user_pokemon_view()
        if user_action == '1':
            self.view.view_all_view(self.user.pokemon)
        elif user_action == '2':
            self.view_by_habitat()
        #Send them back to poke_portal
        self.poke_portal()

    def view_by_habitat(self):
        habitat_of_interest = self.view.habitat_search_view(self.user.pokemon)
        pokemon_names = PokeDao.lookup_by_habitat(habitat_of_interest, self.user.id)
        if pokemon_names = []:
            self.view.search_error_view()
            
        else:
            self.view.search_output(pokemon_names)
        



        


PokeController()




