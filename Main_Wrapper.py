# -*- coding: utf-8 -*-
import requests
import json


class Wrapper:
    def __init__(self, Auth_token):
        self.token = Auth_token
        self.base_url = "https://api.tellonym.me/"
        self.headers = {
                        'accept': 'application/json',
                        'authorization': self.token,
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36',
        }

    def get_user_tells(self, user_id, pos, limit=25):
        """
        Comment: gets a users Tells from a certain position
        Input: user_id and position number of Tell
        Output: List of Posts as Json
        Special: Max Limit is 100, else Server error
        """
        temp_url = self.base_url + "answers/{userID}"
        url = temp_url.format(userID=user_id)
        data = {
                "userId": user_id,
                "pos": pos,
                "limit": limit,
                }
        r = requests.get(url, headers=self.headers, params=data)
        return json.loads(r.content)

    def get_own_tells(self):
        # TODO: Add docu
        """
        Comment: gets all own incoming tells
        Input:
        Output:
        Special:
        """
        url = self.base_url + "tells"
        response = requests.get(url, headers=self.headers)
        return json.loads(response.content)

    def get_followings(self, user_id, pos=0):
        # TODO: add docu
        """
        Comment:
        Input:
        Output:
        Special:
        """
        temp_url = self.base_url + "followings/id/{user_id}"
        url = temp_url.format(user_id=user_id)
        params = {"userId": user_id, "pos": pos}
        r = requests.get(url, params=params, headers=self.headers)
        return json.loads(r.content)

    def get_followers_name(self, username, limit=25, pos=0):
        """
        Comment: get's followers by a username
        Input: Name of Instance, username
        Output: Server Response as Json
        Special: max Limit:500
        """
        temp_url = self.base_url + "followers/name/{username}"
        url = temp_url.format(username=username)
        params = {"limit": limit, "pos": pos}
        r = requests.get(url, params=params, headers=self.headers)
        return json.loads(r.content)

    def get_followers_id(self, user_id):
        # TODO: add docu
        """
        Comment: get's followers by a users id
        Input:
        Output:
        Special:
        """
        temp_url = self.base_url + "followers/id/{user_id}"
        url = temp_url.format(user_id=user_id)
        params = {"userId": user_id, "limit": "27"}
        r = requests.get(url, params=params, headers=self.headers)
        return json.loads(r.content)

    def get_details_id(self, user_id):
        """
        Comment: returns user details by user id
        Input: Name of instance, user_id
        Output: Details as json
        Special: Nothing Special
        """
        temp_url = self.base_url + "profiles/id/{userID}"
        url = temp_url.format(userID=user_id)
        r = requests.get(url, headers=self.headers)
        return json.loads(r.content)

    def get_details_name(self, username):
        """
        Comment: Gets a Persons details by their username
        Input: Name of Instance, username
        Output: Json Reply from server
        Special: Nothing Special
        """
        temp_url = self.base_url + "profiles/name/{username}"
        url = temp_url.format(username=username)
        r = requests.get(url, headers=self.headers)
        return json.loads(r.content)

    def answer_tell(self, tell_id, Reply):
        # TODO: Add comment
        """
        Comment: answer a tell based on it's tellId
        Input: Name of instance, Id of tell, Textreply
        Output: Json Response from Server
        Special: Nothing Special
        """
        url = self.base_url + "answers/create"
        answer = {
                    "limit": 25,
                    "answer": Reply,
                    "tellId": tell_id
                  }
        r = requests.post(url, data=answer, headers=self.headers)
        return json.loads(r.content)

    def create_tell(self, Text, user_id):
        # FIXME: Not working, captcha?
        """
        Comment: create a tell based on the tellId
        Input: Name of instance, Text for tell, UserId
        Output: Server Reply
        Special: currently not working # FIXME:
        """
        url = self.base_url + "tells/new"
        data = {
                    "tell": Text,
                    "userId": user_id,
                    "limit": 25,
                    "isInstagramInAppBrowser": True,
                    "isSenderRevealed": False,
                }
        r = requests.post(url, data=data, headers=self.headers)
        return r.content

    def search_users(self, search_string, limit=25, pos=0):
        """
        Comment: search for users by their username
        Input: Name of Instance, search_string, optional: Limit, max 50
        Output: Result as Json
        Special: Nothing special noticed
        """
        url = self.base_url + "search/users"
        params = {
                "searchString": search_string,
                "limit": limit,
                "pos": pos
                }
        r = requests.get(url, params=params, headers=self.headers)
        return json.loads(r.content)


def main():
    token = json.load(open("creds.json", "r"))["token"]
    test = Wrapper(token)
    # t1 = "'<script>alert('hello')</script>'"
    x = test.search_users("test", 50)
    print x
    json.dump(x, open("out.json", "w"))
    # print len(x["followers"])


if __name__ == '__main__':
    main()
