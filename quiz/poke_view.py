import numpy as np

class PokeView:
    def __init__(self):
        pass

    def home_screen_view(self):
        print('Welcome to the PokeDB. What do you want to do?\n1. Login\n2. Add User')
        return input('>')
        pass


    def new_user_view(self):
        print('What is the username you would like to create?')
        return (input('>'))

    def login_screen_view(self):
        print('What is your username?')
        return input('>')

    def login_error_view(self, error):
        print(error, '...bye.' )

    def poke_portal_view(self):
        print('Welcome! What would you like to do?\n1. View my pokemon\n2. Add Pokemon\n3. Delete Pokemon\n4. Quit')
        return (input('>'))

    def add_pokemon_view(self):
        print('What is the name of the pokemon?')
        poke_name = input('>')
        return poke_name.lower()

    def add_success_view(self):
        print(f'Succesfully added to your record.')


    def delete_pokemon_view(self,user_pokemon_list):
        print('Which pokemon do you want to delete?(use number on left)')
        for i,x in enumerate(user_pokemon_list):
            print(i,x)
        return int(input('>'))

    def delete_succes_view(self):
        print(f'Successfuly removed from your record.')

    def pokemon_add_del_error_view(self):
        input('Pokemon not found. Press any key to return home.')

    def view_user_pokemon_view(self):
        print('How would you like to view your pokemon?\n1. View all\n2. View by habitat')
        return input('>')

    def user_has_no_pokemon_view(self):
        input('uh oh! looks like you have no pokemon. Press any key to return to the portal.')

    def view_all_view(self, pokemon_list):
        print('Below are all of your pokemon:')
        for x in pokemon_list:
            print(x)

    def habitat_search_view(self, pokemon_list):
        habitats = []
        for x in pokemon_list:
            if x.habitat not in habitats:
                habitats.append(x.habitat)
        print('The following habitats exist:, \n', habitats)
        print('Which of the above do you want to search by?(type the string)')
        return input ('>')

    def search_output(self, search_result):
        print('We found:')
        for pokemon in search_result:
            print (pokemon[0])
        input('Press any key to return to the portal.')

    def search_error_view(self):
        input('invalid search. Press any key to return to portal')