from helper import util
import json
import re
from random import randint
print()
util = util.Util


class User:

    def __init__(self):
        pass

    @staticmethod
    def get_users():
        return util.get_api("/users/")

    @staticmethod
    def get_random_user_id():
        users_id = []
        for user in json.loads(User.get_users()):
            users_id.append(user['id'])
        return users_id[randint(1, len(users_id)-1)]

    @staticmethod
    def check_username(listOfAllUsers=""):
        for user in json.loads(listOfAllUsers):
            assert user['username'] != ''

    @staticmethod
    def check_email(listOfAllUsers=""):
        for user in json.loads(listOfAllUsers):
            assert user['email'] != ''

    @staticmethod
    def check_valid_email(listOfAllUsers=""):
        regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        for user in json.loads(listOfAllUsers):
            matches = re.findall(regex, user['email'])
            assert matches.__len__() > 0

    @staticmethod
    def check_catchphrase_length(listOfAllUsers=""):
        for user in json.loads(listOfAllUsers):
            assert user['company']['catchPhrase'].__len__() < 50

    @staticmethod
    def check_name(listOfAllUsers=""):
        for user in json.loads(listOfAllUsers):
            assert user['name'] != ''

    @staticmethod
    def check_zip_code(listOfAllUsers=""):
        for user in json.loads(listOfAllUsers):
            assert user['address']['zipcode'].__len__() != ""

    @staticmethod
    def get_user_by_id(userId):
        for user in json.loads(util.get_api("/users/")):
            if str(user['id']) == str(userId):
                return user
