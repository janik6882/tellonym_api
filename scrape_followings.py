from Main_Wrapper import Wrapper
from collections import Counter
import json
import os
import MySQLdb
import time
import sys
import requests

def main(timeout=2):
    def add_following_to_db(user, following):
        sql = """INSERT INTO Follower_analyse (id, user, following) VALUES(NUll, %s, %s)"""
        val = (user, following)
        try:
            try:
                cursor.execute(sql, val)
            except MySQLdb._exceptions.IntegrityError:
                pass
        except UnicodeEncodeError:
            pass
        db.commit()
    def exit(curr_queue):
        json.dump(curr_queue, open("queue.json", mode="w"))
        sys.exit()
        print ("successful exit")
    def resume():
        return json.load(open("queue.json", mode="r"))
    creds = json.load(open("creds.json", "r"))
    token = creds["token"]
    host = creds["ip"]
    username = creds["user"]
    password = creds["password"]
    database = creds["db"]
    port = creds["port"]
    db = MySQLdb.connect(user=username, passwd=password, db=database, host=host, port=port)
    cursor = db.cursor()
    api = Wrapper(token, proxy=None)
    working = True
    queue = resume()
    request_count = 0
    # print (queue)
    try:
        try:
            while working:
                # print ("working")
                current_user = queue.pop(0)
                print (current_user)
                followings = api.get_followings_name(current_user, limit=500)
                request_count += 1
                print (followings)
                followings = followings["followings"]
                for user in followings: queue.append(user["username"])
                for user in followings: add_following_to_db(current_user, user["username"])
                queue = Wrapper.remove_duplicates_list(queue)
                try:
                    time.sleep(timeout)
                except KeyboardInterrupt:
                    # print (e)
                    print (request_count)
                    exit(queue)
        except KeyboardInterrupt as e:
            print (e)
            print (request_count)
            exit(queue)
    except Exception as e:
        print (e)
        print (request_count)
        exit(queue)


def debug():
    # testing proxy:
    headers = {
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
    proxies = {"https":"http://122.254.87.206:8080"}
    r = requests.get("https://api.tellonym.me/likes/id/1474707237", headers=headers, proxies=proxies)
    print (r.content)


if __name__ == '__main__':
    main(timeout=2)
    # debug()
