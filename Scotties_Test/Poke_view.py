
from getpass import getpass

#This class is for the initial signin/signup processes
class UserView: 

    @staticmethod
    def home_screen(): 

        print("\n Welcome to Your Pokedex! \n")
        print("Do you already have an account? \n")

        answer = input("Y/N: ")

        return_value = UserView.yes_no_validate(answer, "UserView.home_screen()")
        return return_value

    

    @staticmethod
    def signup(): 
    #getting username/password getpass simply makes input invisible
        print("\nWelcome to the Account Creator \n")
        username = input("Please choose a username: ")
        password = getpass()
        return [username, password]

    @staticmethod
    def signin():
        print("\nWelcome Back! \n")
        username = input("Please input your username: ")
        password = getpass()
        return [username, password]

######YES/NO VALIDATORS#########################################
#probably need to be in another class but running short on time#
################################################################

    @staticmethod
    def yes_no_validate_with_argument(answer, func, arg):

        if answer.lower() == "y" or answer.lower() == "yes":  
            return True
        elif answer.lower() == "n" or answer.lower() == "no":
            return False
        else: 
            Error_Messages.yes_no()
            redo = eval(func)
            return redo 

    @staticmethod
    def yes_no_validate(answer, func):

        if answer.lower() == "y" or answer.lower() == "yes": 
            return True 
        elif answer.lower() == "n" or answer.lower() == "no":
            return False
        else: 
        #if a user inputs something other than yes or no it resets the process
            Error_Messages.yes_no()
            redo = eval(func)
            return redo




#######################NEW CLASS LOGGED_IN_VIEW###############################
#this class is used for any of the decision trees once a user is authenticated
##############################################################################

class Logged_In_View: 


    @staticmethod
    def logged_in_menu(): 

        print("""
Now that you are logged in, what would you like to do?

1. Add Pokemon
2. Delete Pokemon
3. View Pokemon
4. View Pokemon by Type
5. View Pokemon by Habitat
6. Exit Pokedex
        """)
        choice = input("Your selection: ")
        #checking that user entered a number
        try:
            choice_check = int(choice)
           
        except ValueError: 
            Error_Messages.yes_no()
            redo = Logged_In_View.logged_in_menu()
            return redo

 
        if int(choice) >= 1 and int(choice) <= 6:
            return choice 
        else: 
            Error_Messages.yes_no()
            redo = Logged_In_View.logged_in_menu()
            return redo

    @staticmethod
    def add_delete_pokemon(expression_type):
        pokemon = input(f"\n Please enter the name of the Pokemon you would like to {expression_type}: ")
        return pokemon

    @staticmethod
    def confirm_add_delete(expression_type):
        answer = input(f"\n Is this the pokemon you would like to {expression_type}? Y/N: ")
        return_value = UserView.yes_no_validate_with_argument(answer, "Logged_In_View.confirm_add_delete(arg)", expression_type)
        return return_value

    @staticmethod
    def view_pokemon(lst, user): 
        #building a new list of lists instead of list of tuples
        user_return = [list(tup) for tup in lst]
        #this calculates the longest word in a row and pads by 2 for formatting
        col_width = max(len(word) for row in user_return for word in row) + 2
        #This left adjusts by the column width calculated for alignment purposes
  
        for row in user_return: 
            out = "".join(word.ljust(col_width) for word in row)
            length = len(out)
            print(out)
            if row == user_return[0]:
                print(length*"=")
        

    @staticmethod
    def search_by_method(value):
        return_value = input(f"\nPlease enter the {value} you would like to search by: ")
        return return_value

    @staticmethod
    def confirm_search_by_method(query, value): 
        confirm = input(f"\n You have selected {query}, are you sure that is the {value} you want to search for? Y/N: ")
        if confirm.lower() == "y" or confirm.lower() == "yes": 
            return True
        elif confirm.lower() == "n" or confirm.lower() == "no":
            return False
        else: 
            Error_Messages.yes_no()
            redo = Logged_In_View.confirm_search_by_method(query, value)
            return redo 

    @staticmethod
    def continue_session(search_value):
        answer = input(f"\n Would you like to search for another {search_value}? Y/N:")
        return_value = UserView.yes_no_validate_with_argument(answer, "Logged_In_View.continue_session(arg)", search_value)
        return return_value
        
        
    @staticmethod
    def add_delete_another(task_type): 
        answer = input(f"\n Would you like to {task_type} another Pokemon? Y/N:")
        return_value = UserView.yes_no_validate_with_argument(answer,"Logged_In_View.add_delete_another(arg)", task_type)
        return return_value


    @staticmethod
    def do_something_else(): 

        answer = input("\n Would you like to do something else before Logging Out? Y/N:")
        return_value = UserView.yes_no_validate(answer, "Logged_In_View.do_something_else()")
        return return_value
    
    @staticmethod
    def logout_Screen():

        answer = input("\n Are you sure you want to Logout? Y/N:")
        return_value = UserView.yes_no_validate(answer, "Logged_In_View.logout_Screen()")
        return return_value
        

    #for when do_something_else is false
    @staticmethod
    def Logged_Out():
        print("\n You've been logged out. See you soon!")




##########NEW CLASS ERROR MESSAGES#############################################################
#Used to return widely used error messages#####################################################
###############################################################################################

class Error_Messages: 

    @staticmethod
    def api_show_error(): 
        print("\n Something went wrong, we can't find that pokemon, try another.")

    @staticmethod
    def not_in_inventory(): 
        print("\n Something went wrong, we can't find that pokemon in your inventory.")
    
    @staticmethod
    def yes_no(): 
        print("\n That is not a valid input!")
