#the initial values of the spy
from termcolor import colored
#class spy defined here
class Spy:
    def __init__(self):

        self.name=colored(' Mr. Sant KS',attrs=['underline','bold'])
        self.age=25,
        self.rating=5.0
#each friend is a dictionary and is stored in the list
james={'name':'Mr. James','age':'20','rating':'4.5','is_online':'True','chats':{'message':['help me'],'date':[],'sent_by_me':False}}
friends=[james]
