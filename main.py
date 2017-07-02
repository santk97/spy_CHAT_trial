#the main file of the application

#importing from spy_details the stored data
from spy_details import spy
#importing from spy_chat_funct the required methods
from spy_chat_funct import start_chat,register_user

print '\t\t\tSPY CHAT'
print 'Welcome Agent!!'
#asking user if he wants to continue as the stored data user
print 'Do you want to continue as ',spy['name'],
choice=raw_input( ' y/n')
if choice.lower()=='y':
    #call to start_chat
    start_chat(spy)
else :
    # call to register_user method
    spy['name'], spy['rating'], spy['age']=register_user()
    start_chat(spy)








