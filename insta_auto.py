from time import sleep
import datetime
import random
from instagram_private_api import Client, ClientCompatPatch

username = "username"   
password =  "password"


try:
    api = Client(username, password)
except Exception as e :
    print(e)
    sleep(random.randint(200, 300))
    pass
def follow():
    f = open('ids.txt', 'r')
    id = f.read()
    id = id.split('/')
    for ids in id:
        api.friendships_create(ids)
        sleep(random.randint(6, 10))
    f.close()
def unfollow():
    f = open('ids.txt', 'r')
    id = f.read()
    id = id.split('/')
    for ids in id:
        api.friendships_destroy(ids)
        sleep(random.randint(6, 10))
    f.close()
def run():
    while True:
        print("Start Follow")
        follow()
        sleep(7200)
        print("Start Unfollow")
        unfollow()
        sleep(7200)

run()
