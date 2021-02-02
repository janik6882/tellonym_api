# -*- coding: utf-8 -*-
import requests
import json
import time


class Wrapper:
    def __init__(self, Auth_token, proxy=None):
        # initialising token
        self.token = Auth_token
        # setting base api url
        self.base = "https://api.tellonym.me/"
        # setting headers
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
        # setting headers for authenticated access only
        self.auth_head = Wrapper.merge_dict(self.headers, {'authorization': self.token})
        # creating sessions for normal and authenticated access
        self.sess = requests.Session()
        self.auth_sess = requests.Session()
        # setting headers for both sessions
        self.sess.headers.update(self.headers)
        self.auth_sess.headers.update(self.auth_head)
        # if proxy, setting proxy for both sessions
        if proxy:
            self.proxy = {"https": proxy}
            self.sess.proxies.update(self.proxy)
            self.auth_sess.proxies.update(self.proxy)
        # self.auth_head = self.headers

    def get_user_tells(self, user_id, pos=0, limit=50):
        """
        Comment: gets a users Tells from a certain position
        Input: user_id and position number of Tell
        Output: List of Posts as Json
        Special: Max Limit is 100, else Server error, No auth required
        """
        temp_url = self.base + "answers/{userID}"
        url = temp_url.format(userID=user_id)
        data = {
                "userId": user_id,
                "pos": pos,
                "limit": limit,
                }
        r = self.sess.get(url, params=data)
        return json.loads(r.content)

    def get_own_tells(self, limit=25, pos=0):
        """
        Comment: gets all own incoming tells
        Input: Name of Instance
        Output: Json object with own tells
        Special: Auth required
        """
        url = self.base + "tells"
        params = {
                "limit": limit,
                "pos": pos
        }
        response = self.auth_sess.get(url, params=params)
        return json.loads(response.content)

    def get_followings_id(self, user_id, pos=0, limit=50):
        """
        Comment: Gets a users followings by their userId
        Input: Name of Instance, userId, optional: position, limit
        Output: Json object with followings
        Special: No auth required, max Limit is 50, else: Server Error
        """
        temp_url = self.base + "followings/id/{user_id}"
        url = temp_url.format(user_id=user_id)
        params = {
                  "userId": user_id,
                  "pos": pos,
                  "limit": limit}
        r = self.auth_sess.get(url, params=params)
        return json.loads(r.content)

    def get_all_followings_id(self, user_id):
        # TODO: add docu
        num_foll = self.get_details_id(user_id)["followingCount"]
        res = []
        for i in range(0, num_foll, 50):
            followings = self.get_followings_id(user_id, pos=i)
            print(followings)
            res += followings["followings"]
        return res

    def get_followings_name(self, user_name, pos=0, limit=50):
        """
        Comment: Gets a users followings by their Username
        Input: Name of instance, Username, optional: position, limit
        Output: Json object with Followings
        Special: No Auth required, max Limit:50, else: Server Error
        """
        temp_url = self.base + "followings/name/{user_name}"
        url = temp_url.format(user_name=user_name)
        params = {
                  "pos": pos,
                  "limit": limit,
                  }
        r = self.auth_sess.get(url,params=params)
        return json.loads(r.content)

    def get_all_followings_name(self, username):
        # TODO: add docu
        details = self.get_details_name(username)
        num_foll = details["followingCount"]
        res = []
        for i in range(0, num_foll, 50):
            followings = self.get_followings_name(username, pos=i)
            print(followings)
            res += followings["followings"]
        return res

    def get_followers_name(self, username, limit=50, pos=0):
        """
        Comment: get's followers by a username
        Input: Name of Instance, username
        Output: Server Response as Json
        Special: No auth required max Limit:50, max pos seems to be 350
        # TODO: research max pos
        """

        temp_url = self.base + "followers/name/{username}"
        url = temp_url.format(username=username)
        params = {
                  "limit": limit,
                  "pos": pos,
                  }
        r = self.auth_sess.get(url, params=params)
        return json.loads(r.content)

    def get_all_followers_name(self, username):
        """
        Comment: gets all followers of a user by their username
        Input: Name of instance, Username
        Output: All followers as Json object
        Special: seems to return maximum of 350 followers
        """
        # TODO: Revisit, check max pos 350
        # BUG: max returned followers is 350, revisit and check
        details = self.get_details_name(username)
        num_foll = details["followerCount"]
        anon_foll = details["anonymousFollowerCount"]
        target = num_foll-anon_foll
        res = []
        for i in range(0, target, 50):
            followers = self.get_followers_name(username, pos=i)
            time.sleep(2)
            res += followers["followers"]
        return res

    def get_followers_id(self, user_id, pos=0, limit=50):
        """
        Comment: get's followers by a users id
        Input: Name of Instance, userId
        Output: Json object with Followers for a user
        Special: max limit is 50, else will result in server error
        """
        temp_url = self.base + "followers/id/{user_id}"
        url = temp_url.format(user_id=user_id)
        params = {
                  "userId": user_id,
                  "limit": limit,
                  "pos": pos,
                  }
        r = self.auth_sess.get(url, params=params)
        return json.loads(r.content)

    def get_all_followers_id(self, user_id):
        """
        Comment: returns all followers for a user by their user_id
        Input: Name of instance, user_id
        Output: all followers as Json object.
        Special: max followers returned seems to be 350. Revisit ans fix
        """
        # BUG: max returned followers is 350, revisit and pot. fix
        details = self.get_details_id(user_id)
        num_foll = details["followerCount"]
        anon_foll = details["anonymousFollowerCount"]
        target = num_foll - anon_foll
        res = []
        for i in range(0, target, 50):
            followers = self.get_followers_id(user_id, pos=i)
            res += followers["followers"]
        return res

    def get_details_id(self, user_id):
        """
        Comment: returns user details by user id
        Input: Name of instance, user_id
        Output: Details as json
        Special: Nothing Special
        """
        temp_url = self.base + "profiles/id/{userID}"
        url = temp_url.format(userID=user_id)
        r = self.sess.get(url)
        return json.loads(r.content)

    def get_details_name(self, username):
        """
        Comment: Gets a Persons details by their username
        Input: Name of Instance, username
        Output: Json Reply from server
        Special: Nothing Special
        """
        temp_url = self.base + "profiles/name/{username}"
        url = temp_url.format(username=username)
        r = self.sess.get(url)
        return json.loads(r.content)

    def answer_tell(self, tell_id, Reply):
        """
        Comment: answer a tell based on it's tellId
        Input: Name of instance, Id of tell, Textreply
        Output: Json Response from Server
        Special: Auth required, currently invalid Token error
        """
        url = self.base + "answers/create"
        data = {
                    "limit": 25,
                    "answer": Reply,
                    "tellId": tell_id
                  }
        r = self.auth_sess.post(url, json=data)
        return json.loads(r.content)

    def create_tell(self, Text, user_id, revealed=False):
        """
        Comment: create a tell based on the tellId
        Input: Name of instance, Text for tell, UserId
        Output: Server reply, which currently doesn't exist (I don't know why)
        Special: if revealed, sender Status must be 2, Auth required
        """
        # TODO: revisit and check functioning
        url = self.base + "tells/new"
        data = {
                    "tell": Text,
                    "userId": user_id,
                    "limit": 25,
                    "isSenderRevealed": revealed,
                }
        if revealed:
            data = Wrapper.merge_dict(data, {"senderStatus": 2})
        r = self.auth_sess.post(url, json=data)
        return r.content

    def search_users(self, search_string, limit=25, pos=0):
        """
        Comment: search for users by their username
        Input: Name of Instance, search_string, optional: Limit, max 50
        Output: Result as Json
        Special: Auth required
        """
        url = self.base + "search/users"
        params = {
                "searchString": search_string,
                "limit": limit,
                "pos": pos
                }
        r = self.auth_sess.get(url, params=params)
        return json.loads(r.content)

    def get_own_friends(self, limit=25, pos=0):
        """
        Comment: get own friends by
        Input: Name of Instance, optional: limit, max 500
        Output: Friends as Json object
        Special: Auth required, Max limit is 500, contraint on server side
        """
        url = self.base + "followings/list"
        params = {
                "limit": limit,
                "pos": pos
                  }
        r = self.auth_sess.get(url, params=params)
        return json.loads(r.content)

    def get_answer_likes(self, answer_id, limit=25):
        """
        Comment: returns the detailed likes for a tellonym answer
        Input: answer_id, optional:Limit
        Output: Details as Json
        Special: Nothing
        """
        temp_url = self.base + "likes/id/{answerId}"
        params = {
                  "limit": limit,
                  }
        url = temp_url.format(answerId=answer_id)
        r = self.sess.get(url, params=params)
        return json.loads(r.content)

    def follow_user_id(self, user_id, anonymous=True, limit=25):
        """
        Comment: follow a user based on their userID
        Input: user_id,optional: bool if anonymous
        Output: Confirmation as Json object
        Special: Auth required
        """
        # FIXME: Fix, currently not working. Error: Wrong parameter data
        url = self.base + "followings/create"
        data = {
                  "isFollowingAnonymous": anonymous,
                  "userId": user_id,
                  "limit": limit,
                 }
        r = self.auth_sess.post(url, json=data)
        return json.loads(r.content)

    def follow_user_name(self, user_name, anonymous=True, limit=25):
        # TODO: add docu
        user_id = self.get_details_name(user_name)["id"]
        res = self.follow_user_id(user_id, anonymous, limit)
        return res

    def unfollow_user_id(self, user_id):
        """
        Comment: destroy follow for user
        Input: Name of instance, userId
        Output: Response as Json object
        Special: Auth required
        """
        url = self.base + "followings/destroy"
        data = {
                "userId": user_id,
                }
        r = self.auth_sess.post(url, json=data)
        return json.loads(r.content)

    def unfollow_user_name(self, user_name):
        # TODO: add docu
        user_id = self.get_details_name(user_name)["id"]
        res = self.unfollow_user_id(user_id)
        return res

    def destroy_tell(self, tell_id, limit=25):
        """
        Comment: delete a tell from your inbox
        Input: Name of instance, tellId, optional:limit
        Output: Server Response, currently nothing (Don't ask me why)
        Special: Auth required
        """
        url = self.base + "tells/destroy"
        data = {
                "tellId": tell_id,
                "limit": limit,
                }
        r = self.auth_sess.post(url, json=data)
        # OMFGRLY: Server response is empty!!
        return r.content

    def get_own_settings(self):
        # TODO: Add docu
        """
        Comment:
        Input:
        Output:
        Special:
        """
        url = self.base + "accounts/settings"
        # TODO: Find further Params
        params = {
                }
        r = self.auth_sess.get(url, params=params)
        return json.loads(r.content)

    def get_own_anouncements(self):
        # TODO: add docu
        """
        Comment:
        Input:
        Output:
        Special:
        """
        url = self.base + "announcements/list"
        params = {
                 }
        r = self.auth_sess.get(url, params=params)
        return json.loads(r.content)

    def check_updates(self):
        # TODO: add docu
        # CHECK: check function
        url = self.base + "check/updates"
        params = {
                 }
        r = self.auth_sess.get(url, params=params)
        return json.loads(r.content)

    def get_own_feeds(self):
        # TODO: add docu
        # CHECK: check function
        url = self.base + "feed/ids"
        params = {}
        r = self.auth_sess.get(url, params=params)
        return json.loads(r.content)

    def get_feeds_olderthan(self, older_than):
        # TODO: Add docu, find missing parameter
        url = self.base + "feed/olderthan"
        params = {
                "id": older_than,
                "oldest": older_than,
                "oldestId": older_than,
                "sortId": older_than,
                # TODO: add param
        }
        r = self.auth_sess.get(url, params=params)
        return r.text

    def get_feed_list(self):
        # TODO: Add docu
        url = self.base + "feed/list"
        params = {}
        r = self.auth_sess.get(url, params=params)
        return json.loads(r.content)

    def get_friend_suggestions(self):
        # TODO: Add docu
        url = self.base + "suggestions/friends"
        params = {}
        r = self.auth_sess.get(url, params=params)
        return json.loads(r.content)

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
    x = test.get_all_followers_id(test_user_id)
    print (x)
    print(len(x))
    json.dump(x, open("out.json", "w"))


if __name__ == '__main__':
    debug()
