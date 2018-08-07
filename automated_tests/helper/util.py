import requests


def _url(path):
    return 'https://jsonplaceholder.typicode.com' + path


class Util:

    def __init__(self):
        pass

    @staticmethod
    def get_api(path=""):
        return requests.get(_url(path)).content

    @staticmethod
    def post_api(path="", data=""):
        return requests.post(_url(path), data)
