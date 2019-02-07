#The main file of the Application

#importing from spy_details the stored data
from spy_details import Spy
#importing term color library
from termcolor import colored,cprint
#importing from spy_chat_funct the required methods
from spy_chat_funct import start_chat,register_user
#class object
spy=Spy()

print colored('           SPY CHAT           ','red','on_grey',attrs=['bold','underline'])
print '\n\n\n'
print colored('\t\tWelcome Agent!!!!','red')
#asking user if he wants to continue as the stored data user
print colored('Do you want to continue as ','green','on_grey'),colored(spy.name,'blue'),
choice=raw_input( colored(' (y/n)','red'))
if choice.lower()=='y':
    #call to start_chat
    start_chat(spy)
else :
    # call to register_user method
    spy.name, spy.rating, spy.age=register_user()
    start_chat(spy)








