#the file with all the methods
#making the necessary imports of file and the libraries
from datetime import datetime
from termcolor import  colored
from spy_details import friends
from steganography.steganography import Steganography
#a list to store the list of statuses
status_list=["Bond...James bond","Desperate time....Desperate measures"]
special_words=["help","help me ","Save me ","mission failed","spy killed","spy caught",'intruders',"SOS","code 49"]

#start_chat method to display menu and work according to the choice of the user

def start_chat(spy) :
    status=None
    print colored('Welcome '+ colored(spy.name,'blue',attrs=['blink']),'green','on_grey')
    menu_choice = 1
    while menu_choice != 6:
        #the main menu for the user
        help_messages()
        print colored('Menu \n 1.Status Update  \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read old chats \n 6. Close application\n \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t ','green','on_grey')
        menu_choice = int(raw_input(colored('Enter a choice\n','green','on_grey')))
        #calling respective methods according to the input
        if menu_choice == 1:
            status =status_update(status)
        elif menu_choice == 2:

            friend_list()

        elif menu_choice == 3:

            location=select_friend()
            send_message(location)

        elif menu_choice == 4:

            decode_message()

        elif menu_choice == 5:

            location = select_friend()
            read_message(location)

        elif menu_choice == 6:
            print colored('QUITTING!!!!!','red','on_green',attrs=['bold','underline'])
        else:
            print colored('invalid choice!!!','red','on_grey',attrs=['bold'])

    return 0

#register_user method to enter the details of the new user
def register_user():
    # store the name in variable spy_name
    spy_name = raw_input(colored('Please enter your name ','green','on_grey'))
    # validating the inputs
    while len(spy_name) == 0:
        print colored('name cannot be empty','red','on_grey')
        spy_name = raw_input(colored('Enter a valid name ','red','on_grey'))

    # Set the salutation for the user
    salutation=raw_input(colored('How should we address you (Mr./Mrs./Ms.)','green','on_grey'))
    spy_name=salutation+'  '+spy_name
    # Getting other details from the user

    print colored('Well , hello  '+ colored(spy_name,'blue','on_grey') +colored(' great to have you back ....','green','on_grey'),'green','on_grey')
    print colored('we would like to know a little more about you..','green','on_grey')

    # ask the user to inout the age and check if it is valid
    spy_age = int(raw_input(colored('how old are you : ','green','on_grey')))
    if spy_age < 12:
        print colored(' Too young to be an agent .....sorry','yellow','on_grey')
        exit()
    if spy_age > 50:
        print colored(' You need to retire now ....Goodbye ','yellow','on_grey')
        exit()

    # ask the user about the rating and greet him accordingly
    spy_rating = float(raw_input(colored('what is your spy rating ','green','on_grey')))
    if spy_rating > 4.7:
        print colored('You are one of our special agengts .....We are lucky to have you','green','on_grey')
    elif spy_rating > 3.5 and spy_rating <= 4.7:
        print colored('You are one of the best agents we have ','green','on_grey')
    elif spy_rating < 3.5 and spy_rating > 2.7:
        print colored('Welcome Agent .....you have a lot to prove','green','on_grey')
    # show the spy details if he wants to stay online
    spy_is_online = True
    spy_stat = raw_input(colored('do you want to stay online y/n','green','on_grey'))

    if (spy_stat.lower() == 'y'):
        spy_is_online = True
        print colored('You are now Online .....','green','on_grey')

    # if not he can log off
    else:
        print colored('Goodbye ....we will see you soon ...','red','on_grey')
        exit()
    return spy_name,spy_rating,spy_age

#method to update the status of the spy
def status_update(status):
    #print the current status
    print colored('Status : ','green','on_grey') ,colored( status,'blue','on_grey')
    if (status)==None:
        print colored('status is empty','yellow','on_grey')

    ch=raw_input(colored('Do you want to update your status (y/n)','green','on_grey'))
    if ch.lower()=='y':
        ch=int(raw_input(colored('1.Add a new status\n2.Choose from an old one \n','green','on_grey')))
        if ch==1:
            #adding a new status to be entered by the user e
            new_status=raw_input(colored('New status: ','green','on_grey'))
            while len(new_status)==0:
                print colored('Empty status !!!','red','on_grey')

            status=new_status
            #using the append method to update the list of statuses
            status_list.append(new_status)
        elif ch==2 :
            i=1
            #using for loop to print the list of all the statuses entered by user in the past
            for temp in status_list:
                print colored(str(i)+'.','red','on_grey'), colored(temp,'white','on_grey')
                i=i+1
             #upodating status from the previous record of the statuses
            select=int(raw_input(colored('choose the status you want to set','green','on_grey')))
            status=status_list[select-1]
        print colored('Updated Status: ','green','on_grey'),colored(status,'magenta','on_grey')
    elif ch.lower()=='n' :
        print colored('Back to main menu....','green','on_grey')
    else:
        print colored("INVALID ENTRY",'red','on_grey')
        start_chat()
     #returning the new status so that it can be updated in the main app
    return status

def friend_list():
    #creating  a temp dictionary
    temp_friend={
        'name':''
        ,'age':'',
        'rating':'',
        'is_online':'True',
        'chats':{'message':[],'date':[],'sent_by_me':False}
    }
  #printing the friends details
    print colored('Friend List \n You have ','green','on_grey'),colored(len(friends),'red'),colored(' friends','green','on_grey')
    ch=int(raw_input( colored('\n what would you like to do \n 1. View Friend list \n 2. Add a new friend ','green','on_grey')))

    if ch==1:
        i=1
        print colored('  Name \t\t    Age   Rating ','yellow','on_grey')
        for temp_friend in friends:
            print colored(str(i)+'.','red','on_grey'),colored (temp_friend['name'] + '\t  ','blue','on_grey'),colored(temp_friend['age'],'magenta','on_grey'),colored('\t ' +str(temp_friend['rating']),'yellow','on_grey')

            i=i+1
    else :
        add_friend()

#this method adds the friend to the list
def add_friend():
    #storing the details of a new friend , validating it and adding him/her
        new_friend={
            'name':'',
            'age':'',
             'rating':'',
            'is_online':'True',
            'chats':{'message':[],'date':[],'sent_by_me':False}
        }
        print colored('Add the details of the friend','green','on_grey')
        while len(new_friend['name'])==0:
            new_friend['name']=raw_input(colored("Name of the friend",'green','on_grey'))
            new_friend['age']=int(raw_input(colored('Age of the friend','green','on_grey')))
            new_friend['rating'] =float(raw_input(colored('Spy rating of the friend','green','on_grey')))

        print colored("Friend's data has been succesfully upated",'yellow','on_grey')
        friends.append(new_friend)

#this method returns the index of the friend in the friend list
def select_friend():
    print colored('Select from the friend list  ','green','on_grey')
    print colored('Friend List \n You have ', 'green', 'on_grey'), colored(len(friends), 'red'), colored(' friends','green','on_grey')


    temp_friend = {
        'name': ''
        , 'age': '',
        'rating': '',
        'chats':{'message':[],'date':[],'sent_by_me':False}
    }

    i = 1
    print colored('  Name \t\t    Age   Rating ', 'yellow', 'on_grey')
    for temp_friend in friends:
        print colored(str(i) + '.', 'red', 'on_grey'), colored(temp_friend['name'] + '\t  ', 'blue',
                                                               'on_grey'), colored(temp_friend['age'], 'magenta',
                                                                                   'on_grey'), colored(
            '\t ' + str(temp_friend['rating']), 'yellow', 'on_grey')

        i = i + 1
    index= int(raw_input( colored(' Select the friend  ','green','on_grey')))
    return index-1
#method to select a friend and send a message
def send_message(index):
    text=raw_input(colored('Enter the message you want to send','green','on_grey'))
    input=raw_input(colored('select the image for encoding','green','on_grey'))
    output='output.jpg'
    Steganography.encode(input,output,text)
    temp_friend={
        'chats':{'message':[],'sent_by_me':False,'date':[]}
    }
    #using the date time library
    date=datetime.now()
    dated=date.strftime("%a, %d %b %Y %H:%M")
    #using the steganography library
    text=Steganography.decode(output)
    temp_friend=friends[index]
    temp_friend['chats']['sent_by_me']=True
    temp_friend['chats']['message'].append(text)
    temp_friend['chats']['date'].append(dated)
    print colored('the message has been sent to ','yellow','on_grey'),colored(temp_friend['name'],'red','on_grey')

#method to read older chats with friend
def read_message(index):
    temp_friend={
        'name':'',
        'chats': {'message': [], 'sent_by_me': False,'date':[]}
    }
    temp_friend=friends[index]
    print colored(' the conversation with %s  ','green','on_grey')%colored(temp_friend['name'],'red','on_grey')
    if temp_friend['chats']['sent_by_me']==True:
        i=0
        for temp in temp_friend['chats']['message']:
                print colored(temp_friend['chats']['date'][i],'magenta','on_grey'),colored('You said: ','yellow','on_grey'),colored(temp+'\n','cyan','on_grey')
                i=i+1

    else :
        i = 0
        for temp in temp_friend['chats']['message']:
            print colored(temp_friend['chats']['date'][i],'magenta','on_grey'),colored('He said: ','yellow','on_grey'), colored(temp+'\n','blue','on_grey')
            i = i + 1
#method to decode any secret image messages
def decode_message():
    output=raw_input(colored('enter the path of the image you want to decode ','green','on_grey'))
    text=Steganography.decode(output)
    print colored('Select the sender of this message','green','on_grey')
    index=select_friend()
    date = datetime.now()
    dated = date.strftime("%a, %d %b %Y %H:%M")
    temp_friend = friends[index]
    temp_friend['chats']['sent_by_me'] = False
    temp_friend['chats']['message'].append(text)
    temp_friend['chats']['date'].append(dated)
    print colored('the secret message is ','green','on_grey'), colored(text,'blue','on_grey')

#method to check for special messages
def help_messages():

    print colored('Checking if you have any special messages....','green','on_grey')
    for temp_friend in friends:
        for temp in special_words:
              for  temp_mesage in temp_friend['chats']['message']:
                  if temp==temp_mesage:
                        print colored("YOU HAVE AN URGENT MESSAGE  ", 'red', 'on_grey')
                  else :
                      check=False

    if check==False:

        print colored('You have no urgent messages ', 'green', 'on_grey')