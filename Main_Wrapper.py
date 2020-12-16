# -*- coding: utf-8 -*-
import requests
import json


class Wrapper:
    def __init__(self, Auth_token, proxy=None):
        if proxy:
            self.proxy = {"https": proxy}
        else:
            self.proxy = proxy
        self.token = Auth_token
        self.base_url = "https://api.tellonym.me/"
        self.headers = {
                        "Host": "api.tellonym.me",
                        'accept': 'application/json',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
                        'Origin': 'https://tellonym.me',
                        'Connection': 'keep-alive',
                        'Pragma': 'no-cache',
                        'TE': 'Trailers',
                        'Cache-Control': 'no-cache',
                        "tellonym-client": "web:0.51.1",
        }
        self.auth_head = Wrapper.merge_dict(self.headers, {'authorization': self.token})
        # self.auth_head = self.headers

    def get_user_tells(self, user_id, pos=0, limit=25):
        """
        Comment: gets a users Tells from a certain position
        Input: user_id and position number of Tell
        Output: List of Posts as Json
        Special: Max Limit is 100, else Server error, No auth required
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

    def get_own_tells(self, limit=25, pos=0):
        """
        Comment: gets all own incoming tells
        Input: Name of Instance
        Output: Json object with own tells
        Special: Auth required
        """
        url = self.base_url + "tells"
        params = {
                "limit": limit,
                "pos": pos
        }
        response = requests.get(url, headers=self.auth_head, params=params)
        return json.loads(response.content)

    def get_followings_id(self, user_id, pos=0, limit=25):
        """
        Comment: Gets a users followings by their userId
        Input: Name of Instance, userId, optional: position, limit
        Output: Json object with followings
        Special: No auth required, max Limit is 500, else: Server Error
        """
        temp_url = self.base_url + "followings/id/{user_id}"
        url = temp_url.format(user_id=user_id)
        params = {"userId": user_id, "pos": pos, "limit": limit}
        r = requests.get(url, params=params, headers=self.headers)
        return json.loads(r.content)

    def get_followings_name(self, user_name, pos=0, limit=25):
        """
        Comment: Gets a users followings by their Username
        Input: Name of instance, Username, optional: position, limit
        Output: Json object with Followings
        Special: No Auth required, max Limit:500, else: Server Error
        """
        temp_url = self.base_url + "followings/name/{user_name}"
        url = temp_url.format(user_name=user_name)
        params = {"pos": pos, "limit": limit}
        r = requests.get(url, headers=self.headers, params=params, proxies=self.proxy)
        return json.loads(r.content)

    def get_followers_name(self, username, limit=25, pos=0):
        """
        Comment: get's followers by a username
        Input: Name of Instance, username
        Output: Server Response as Json
        Special: No auth required max Limit:500
        """
        temp_url = self.base_url + "followers/name/{username}"
        url = temp_url.format(username=username)
        params = {"limit": limit, "pos": pos}
        r = requests.get(url, params=params, headers=self.headers)
        return json.loads(r.content)

    def get_followers_id(self, user_id):
        """
        Comment: get's followers by a users id
        Input: Name of Instance, userId
        Output: Json object with Followers for a user
        Special: No auth required
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
        """
        Comment: answer a tell based on it's tellId
        Input: Name of instance, Id of tell, Textreply
        Output: Json Response from Server
        Special: Auth required, currently invalid Token error
        """
        url = self.base_url + "answers/create"
        data = {
                    "limit": 25,
                    "answer": Reply,
                    "tellId": tell_id
                  }
        r = requests.post(url, json=data, headers=self.auth_head)
        return json.loads(r.content)

    def create_tell(self, Text, user_id, revealed=False):
        # FIXME: Not working, captcha?
        """
        Comment: create a tell based on the tellId
        Input: Name of instance, Text for tell, UserId
        Output: Server reply, which currently doesn't exist (I don't know why)
        Special: if revealed, sender Status must be 2, Auth required
        """
        # CHECK: Check, why not working
        # CHECK: check, if no auth required
        url = self.base_url + "tells/new"
        data = {
                    "tell": Text,
                    "userId": user_id,
                    "limit": 25,
                    "isSenderRevealed": revealed,
                }
        if revealed:
            data = Wrapper.merge_dict(data, {"senderStatus": 2})
        r = requests.post(url, json=data, headers=self.auth_head)
        return r.content

    def search_users(self, search_string, limit=25, pos=0):
        """
        Comment: search for users by their username
        Input: Name of Instance, search_string, optional: Limit, max 50
        Output: Result as Json
        Special: Auth required
        """
        url = self.base_url + "search/users"
        params = {
                "searchString": search_string,
                "limit": limit,
                "pos": pos
                }
        r = requests.get(url, params=params, headers=self.auth_head)
        return json.loads(r.content)

    def get_own_friends(self, limit=25, pos=0):
        """
        Comment: get own friends by
        Input: Name of Instance, optional: limit, max 500
        Output: Friends as Json object
        Special: Auth required, Max limit is 500, contraint on server side
        """
        url = self.base_url + "followings/list"
        params = {
                "limit": limit,
                "pos": pos
                  }
        r = requests.get(url, params=params, headers=self.auth_head)
        return json.loads(r.content)

    def get_answer_likes(self, answer_id, limit=25):
        """
        Comment: returns the detailed likes for a tellonym answer
        Input: answer_id, optional:Limit
        Output: Details as Json
        Special: Nothing
        """
        temp_url = self.base_url + "likes/id/{answerId}"
        params = {
                  "limit": limit,
                  }
        url = temp_url.format(answerId=answer_id)
        r = requests.get(url, headers=self.headers, params=params)
        return json.loads(r.content)

    def follow_user(self, user_id, anonymous=True, limit=25):
        """
        Comment: follow a user based on their userID
        Input: user_id,optional: bool if anonymous
        Output: Confirmation as Json object
        Special: Auth required
        """
        # FIXME: Fix, currently not working. Error: Wrong parameter data
        url = self.base_url + "followings/create"
        data = {
                  "isFollowingAnonymous": anonymous,
                  "userId": user_id,
                  "limit": limit,
                 }
        # data = '{userId:67717311,isFollowingAnonymous:true,limit:25}'
        r = requests.post(url, json=data, headers=self.auth_head)
        return json.loads(r.content)

    def unfollow_user(self, user_id):
        """
        Comment: destroy follow for user
        Input: Name of instance, userId
        Output: Response as Json object
        Special: Auth required
        """
        url = self.base_url + "followings/destroy"
        data = {
                "userId": user_id,
                }
        r = requests.post(url, json=data, headers=self.auth_head)
        return json.loads(r.content)

    def destroy_tell(self, tell_id, limit=25):
        """
        Comment: delete a tell from your inbox
        Input: Name of instance, tellId, optional:limit
        Output: Server Response, currently nothing (Don't ask me why)
        Special: Auth required
        """
        url = self.base_url + "tells/destroy"
        data = {
                "tellId": tell_id,
                "limit": limit,
                }
        r = requests.post(url, json=data, headers=self.auth_head)
        return r.content

    @classmethod
    def merge_dict(self, dict_1, dict_2):
        """
        Comment: Merge two dicts
        Input: Name of Instance, dictionary 1, dictionary 2
        Output: A merged dictionary
        Special: Nothing special
        """
        z = dict_1.copy()
        z.update(dict_2)
        return z

    @classmethod
    def remove_duplicates_list(self, inp_list):
        """
        Comment: utility function for removing duplicates from a List
        Input: List, from which duplicates should be removed
        Output: List with removed duplicates
        Special: Nothing special
        """
        res = list(dict.fromkeys(inp_list))
        return res



def debug():
    token = json.load(open("creds.json", "r"))["token"]
    inp = json.load(open("input.json", "r"))
    test = Wrapper(token)
    text = inp["text"]
    test_user_id = inp["userId"]
    test_name = inp["userName"]
    test_answer = inp["testAnswer"]
    test_tell = inp["testTell"]
    test_follow = inp["testFollow"]
    x = test.answer_tell("change, just a sample", "Random stuff.")
    print (x["tells"][0])
    json.dump(x, open("out.json", "w"))


if __name__ == '__main__':
    debug()
