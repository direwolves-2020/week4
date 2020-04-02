
class View: 

    @staticmethod
    def home_screen():
        response = input("""
Welcome to Movie Search! 
Please enter the movie you are looking for: """)
        return response

    @staticmethod
    def search_result(): 
        option = input("If your movie is in this list please input it's number: ")
        return option 

    @staticmethod
    def more_info(): 
        choice = input("Is this the movie you want more info on? Y/N: ")
        if choice.lower() == "y" or choice.lower() == "yes": 
            return True 
        elif choice.lower() == "n" or choice.lower() == "no": 
            return False 
        else: 
            return "Invalid input"


