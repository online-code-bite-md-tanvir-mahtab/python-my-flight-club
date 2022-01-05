import requests

class Store:
    def __init__(self) -> None:
        pass
    def input_data(self,first_name,last_name,email):
        # we will do something
        SHETY_ENDPOINT = "https://api.sheety.co/e78e679bf4063c1cfa9e4f16869c45b0/flightDeals/user"
        SHETY_BODY = {'user':{
            'firstName': first_name,
            'lastName': last_name,
            'email':email,
        }}
        store = requests.post(url=SHETY_ENDPOINT,json=SHETY_BODY)
        print("The data is saved")

    # for getting the data we are going to do this
    def get_the_data(self):
        SHETY_ENDPOINT = "https://api.sheety.co/e78e679bf4063c1cfa9e4f16869c45b0/flightDeals/user"

        data = requests.get(url=SHETY_ENDPOINT)
        return data.json()['user']
