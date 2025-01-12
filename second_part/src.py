#Your code here

#-----------------------------------------------------------------------------------------------------------------------------#
#task 1

import requests
import json

def http_request():


    url='https://europe-west1-dataimpact-preproduction.cloudfunctions.net/recruitement_test_requests?task=1'
    headers = {
        'Accept': 'application/json'  
    }

    response = requests.get(url, headers=headers)

    
    response_result=json.loads(response.text.encode('ascii','ignore').decode('utf-8'))
    response_result['status_code']=(response.status_code)
    return response_result 

# print(http_request())

#-----------------------------------------------------------------------------------------------------------------------------#
#task 2

import requests

def improve_curl():

    # CHANGED THE USER AGENT WHICH CREATES THE CONFLICT
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',

    }

    params = {
        'task': '2',
    }

    response = requests.get(
        'https://europe-west1-dataimpact-preproduction.cloudfunctions.net/recruitement_test_requests',
        params=params,
        headers=headers,
    )

    return response.status_code

# print(improve_curl())

#-------------------------------------------------------------------------------------------------------------------------------------------#
#task 3
import datetime


def format_date(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.strftime("%Y-%m/%d")  # Formatting as 'yyyy-mm/d'
    return wrapper


@format_date
def first_day_last_week():
  
    current_date = datetime.datetime.today()
    current_month = current_date.month
    current_year = current_date.year


    # current month - no. of days
    
    if current_month in [1, 3, 5, 7, 8, 10, 12]:
        days_in_current_month = 31
    elif current_month in [4, 6, 9, 11]:
        days_in_current_month = 30
    else: 
        days_in_current_month = 29

    # last day of the month 
    last_day_of_month = datetime.datetime(current_year, current_month, days_in_current_month)

    ## last day of the week 

    last_day_weekday = last_day_of_month.weekday()

    days_till_sunday = (last_day_weekday) % 7  

    first_day_last_week_ = last_day_of_month - datetime.timedelta(days=days_till_sunday)

    return first_day_last_week_


# print(first_day_last_week())


#---------------------------------------------------------------------------------------------------------------------------------------#

# task 4

class CacheDecorator:
    """Saves the results of a function according to its parameters"""
    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]
        return _wrap



#---------------------------------------------------------------------------------------------------------------------------------------#


# task 5
class LoginMetaClass(type):
    def __new__(cls, name, bases, dct):
        for key, value in dct.items():
            if callable(value) and key != '__init__':
                dct[key] = cls.wrap_method(value)
        return super().__new__(cls, name, bases, dct)

    @staticmethod
    def wrap_method(method):
        def wrapped(self, *args, **kwargs):
            if not getattr(self, 'logged_in', False):
                raise PermissionError("Access denied: You must be logged in.")
            return method(self, *args, **kwargs)

        return wrapped


class AccessWebsite(metaclass=LoginMetaClass):
    logged_in = False

    def login(self, username, password):
        if username == "admin" and password == "admin":
            self.logged_in = True

    def access_website(self):
        return "Success"


