from model import DAO
from view import View

class Controller: 

    def __init__(self): 
            self.view = View()
            self.model = DAO()


    def run(self): 

        title = View.home_screen()

        search = self.search(title)

        answer = View.more_info()

        if answer == True:
            self.title_search(search)
        # elif answer == False:
        #     self.rerun()
        # else:
        #     print("There was an error!")




    def search(self, search): 

        # takes search value and performs an s search 
        query = DAO.get_request(search)

        # builds list of potential movies
        result_lst = DAO.show_results(query)

        #shows the movie list and asks for specific movie 
        client_selection = View.search_result()

        #shows the specific movie client selected
        result = DAO.show_selection(client_selection, result_lst)

        return result

    def title_search(self, search): 
        DAO.specific_search(search)

        










instance = Controller()
instance.run()

