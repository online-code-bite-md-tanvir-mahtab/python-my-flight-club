import requests
from store import Store
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
import time

COUNTRY_CODE= ' '
MESSAGE = ' '

def lowest_price_calculator(low_price,prices : list) -> int:
    low_price = low_price
    # print(low_price)
    for money in prices:
        # print(type(money))
        if low_price>=money:
            low_price = money
        else:
            low_price = 0

    return low_price


def price_destribution(country_code,low_price) -> int:
    # print(country_code)
    prices = []
    data = FlightData()
    if country_code == None:
        pass
    else:
        
        list_data = data.get_data(country_code)
        if len(list_data) == 0:
            pass
        else:
            for p in range(len(list_data)):
                prices.append(list_data[p]['price'])
    return lowest_price_calculator(low_price,prices)

def proces_the_work(f_name,mail):
    data = DataManager().get_data()

    for i in range(len(data)):
        city_name = data[i]['city']
        low_price = data[i]['lowestPrice']
        # print(city_name , "->" , low_price)
        country = FlightSearch()
        city_code = country.get_country_code(city_name)
        
        if city_code is None:
            COUNTRY_CODE = city_name
            l_price = price_destribution(COUNTRY_CODE,low_price)
            MESSAGE = f"Low price alart! Only ${l_price} to fly from Bangladesh-BD to {city_name}-{COUNTRY_CODE}"
        else:
            # print(city_code)
            COUNTRY_CODE = city_code
            l_price = price_destribution(COUNTRY_CODE,low_price)
            # print(l_price)
            MESSAGE = f"dear {f_name}, Low price alart! Only ${l_price} to fly from Bangladesh-BD to {city_name}-{COUNTRY_CODE}"

        # creating the instance of theh notification manager
        notify = NotificationManager()

        print(notify.send_mail(mail,MESSAGE))


is_mail_correct = False
# geting some info from the user
user_name = input("What is your first name :")
user_last_name = input("What is your last name :")
real_mail = input("What is your email :")
retype_mail = input("Type your email again :")

# checking if the real email is mathes with the retype
if real_mail == retype_mail:
    print('You\'re in the club')
    is_mail_correct = True
else:
    print('You\'re typed the wrong mail!! please type the right one')


if is_mail_correct:
    data_storing = Store()
    data_storing.input_data(user_name,user_last_name,real_mail)
    time.sleep(3)
    datas = data_storing.get_the_data()
    for item in datas:
        proces_the_work(item['firstName'],item['email'])
else:
    pass


