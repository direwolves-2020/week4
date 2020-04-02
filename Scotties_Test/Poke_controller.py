# I would like to do a single line multi import but doesnt seem to work
#ex. from poke_view import Uservie, Logged_in_view as UV, LIV

from Poke_view import UserView as UV
from Poke_view import Logged_In_View as LIV
from Poke_view import Error_Messages as EMV
from Poke_model import DAO
from Poke_model import User
import sys

class Controller: 

    #create instance, mainly use to pass around current user
    def __init__(self): 
        self.user = None
        self.logic = None

    #app starts with home screen with login/create account
    def start_app(self):
        session = UV.home_screen()
        if session == False: 
            self.register_user()
        if session == True: 
            self.returning_user()

    #if a user needs a new account
    def register_user(self): 
        user = UV.signup()
        user = User(user[0], user[1])
        DAO.create_user(user)
        self.user = user
        self.logic = Task_Logic(user)
        self.logic.logged_in()
        
    #if a user exists
    def returning_user(self): 
        user = UV.signin()
        user = User(user[0], user[1])
        self.user = user
        self.logic = Task_Logic(user)
        authenticate = DAO.check_login(user)
        if authenticate == False: 
            self.returning_user()
        elif authenticate == True: 
            self.logic.logged_in()
            
        # elif choice == "6": 



#not sure if this was necessary, but it works and I really don't want to refactor again
#basically made this to condense the Controller class
class Task_Logic(Controller):

    def __init__(self, user = None): 
        self.user = user

  
    #logic for option selection on home screen
    def logged_in(self): 
        choice = LIV.logged_in_menu()

        if choice == "1": 
            self.choice1()

        elif choice == "2":
            self.choice2()

        elif choice == "3":
            self.choice3()

        elif choice == "4": 
            self.choice4()

        elif choice == "5": 
            self.choice5()

        elif choice == "6":
            self.choice6()

#built evaluators for this logic using eval and exec, would prefer
# to user higher order functions but could not figure it out 

    def choice1(self):
        pokemon = LIV.add_delete_pokemon("add")
        self.e_add_delete(pokemon, "DAO.create_pokemon(pokemon_to_handle, self.user)", 
                        "self.choice1()", "add")

    def choice2(self):

        pokemon = LIV.add_delete_pokemon("delete")
        self.e_add_delete(pokemon, "DAO.delete_pokemon(pokemon_to_handle, self.user)",
                        "self.choice2()", "delete")
        
    def choice3(self):
        user_query = DAO.view_pokemon(self.user)
        LIV.view_pokemon(user_query, self.user)

        do_something_else = LIV.do_something_else()
        
        self.e_do_something_else(do_something_else)
    
    def choice4(self):
        type_selection = LIV.search_by_method("Pokemon Type")
        self.e_view_by(type_selection, "DAO.get_type(value)",
                        "DAO.view_pokemon_by_type(self.user, value)",
                        "self.choice4()", "Pokemon Type")
        
    def choice5(self):
       #typeselect
        habitat = LIV.search_by_method("Pokemon Habitat")
        self.e_view_by(habitat, "DAO.get_pokemon_habitat(value)",
                        "DAO.view_pokemon_by_habitat(self.user, value)",
                        "self.choice5()", "Pokemon Habitat")
    
    def choice6(self): 
        logout = LIV.logout_Screen()
        if logout == True: 
            LIV.Logged_Out()
            sys.exit(0)
        elif logout == False:
            self.logged_in()

#################################################################
#########EVALUATORS##############################################
#thought about making an Evaluators class but would complicate
#the parent child nature of where they are called from 
################################################################

    def e_continue(self, value, function_select): 

        if value == True: 
            exec(function_select)
        elif value == False: 
            do_something_else = LIV.do_something_else()

        self.e_do_something_else(do_something_else)

    
    def e_do_something_else(self, value):

        if value == True:
            self.logged_in()
        elif value == False:
            LIV.Logged_Out()
            sys.exit(0)

    def e_add_delete(self, pokemon, call1, call2, expression):

        valid_entry = False
        while valid_entry == False: 
            
            api_query = DAO.get_pokemon_name(pokemon)
            if api_query == False: 
                EMV.api_show_error()
                pokemon = LIV.add_delete_pokemon(expression)
            elif api_query != False:
                pokemon_to_handle = DAO.show_pokemon(api_query)
                valid_entry = True
            
        confirm = LIV.confirm_add_delete(expression)
        final_decision = False
        while final_decision == False:
            if confirm == True: 
                eval(call1)
                final_decision = True
            elif confirm == False: 
                exec(call2)
                break

        continues = LIV.add_delete_another(f"{expression}")
        self.e_continue(continues, call2)
            

    def e_view_by(self, value, call1, call2, call3, search_type):   
        valid_entry = False
        while valid_entry == False: 
            api_query = eval(call1)
            if api_query == False: 
                EMV.api_show_error()
                value = LIV.search_by_method(search_type)
            elif api_query != False:
                valid_entry = True
            
        confirm = LIV.confirm_search_by_method(value, search_type)
        final_decision = False
        while final_decision == False:
            if confirm == True: 
                search_result = eval(call2)
                if search_result == False: 
                    
                    break
                LIV.view_pokemon(search_result, self.user)
                final_decision = True
            elif confirm == False: 
                exec(call3)
                break
            

        continues = LIV.continue_session(f"{search_type}")

        self.e_continue(continues, call3)
        
    

        

con = Controller()
con.start_app()

