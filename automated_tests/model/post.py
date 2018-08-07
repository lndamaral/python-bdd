from helper.util import Util
import json


class Post:

    def __init__(self):
        pass

    @staticmethod
    def new_post(user_id, title, body):
        if title == "":
            raise (Exception('Title should not be empty'))

        data = {'userId': '%s' % user_id, "title": '%s' % title, "body": '%s' % body}
        return Util.post_api("/posts/", data).text

    @staticmethod
    def get_post_id_from_response(response_post):
        return json.loads(response_post)['id']

