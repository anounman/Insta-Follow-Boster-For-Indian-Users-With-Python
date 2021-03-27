from time import sleep
import datetime
import random
from instagram_private_api import Client, ClientCompatPatch

username = "username"   
password =  "password"


try:
    api = Client(myAccount, myPassword)
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
        unfollow()
        sleep(3600)
        follow()
        sleep(3600)

run()