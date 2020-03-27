import requests

class Request(): 

    @staticmethod
    def add(num1, num2):
        parameters = {
            'num1': num1,
            'num2': num2
        }

        response = requests.get("http://localhost:5000/add", params=parameters)
        json_response = response.json()

        if response.status_code != 200:
            return 
        else:
            result = "Expression: " + str(json_response['expression']) + "\nResult: " + str(json_response['result'])
        return result


    @staticmethod
    def subtract(num1, num2):
        parameters = {
            'num1': num1,
            'num2': num2
        }

        response = requests.get("http://localhost:5000/subtract", params=parameters)
        json_response = response.json()

        if response.status_code != 200:
            return 
        else:
            result = "Expression: " + str(json_response['expression']) + "\nResult: " + str(json_response['result']) + "\n"
        return result


add = Request.add(5, 5)
subtract = Request.subtract(2, 3)
print(add)
print(subtract)
