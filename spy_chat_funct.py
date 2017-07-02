#the file with all the methods
from datetime import datetime
from spy_details import friends
from steganography.steganography import Steganography
#a list to store the list of statuses
status_list=[]

#start_chat method to display menu and work according to the choice of the user
def start_chat(spy) :
    status=None
    print 'Welcome ', spy['name']
    menu_choice = 1
    while menu_choice != 6:
        #the main menu for the user
        print 'Menu \n 1.Status Update  \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read old chats \n 6. Close application \n '
        menu_choice = int(raw_input('Enter a choice'))
        if menu_choice == 1:
            #call to status_update method
            status =status_update(status)
        elif menu_choice == 2:
            friend_list()

        elif menu_choice == 3:
            print 'send a message '
            location=select_friend()
            send_message(location)
        elif menu_choice == 4:
            print'read a message'
        elif menu_choice == 5:
            print'read old chats'
        elif menu_choice == 6:
            print 'quitting'
        else:
            print 'invalid choice'

    return 0

#register_user method to enter the details of the new user
def register_user():
    # store the name in variable spy_name
    spy_name = raw_input('Please enter your name ')
    # conditional statement to check if the user has left the name blank
    while len(spy_name) == 0:
        # if blank tge user has to enter a valid name
        print 'name cannot be empty'
        spy_name = raw_input('Enter a valid name ')

    gender = raw_input('what is your gender M/F  ')
    # ask the user about the gender and put the respective salutation
    if (gender.upper() == 'M'):
        # print 'Hello Mr. ',spy_name
        spy_name = 'Mr.' + spy_name
    else:
        spy_name = 'Ms.' + spy_name

    # now we will welcome the agent and ask about  other details

    print 'Well , hello', spy_name, ' great to have you back ....'
    print 'we would like to kn ow a little more about you..'
    # ask the user to inout the age and check if it is valid
    spy_age = int(raw_input('how old are you : '))
    # print type(spy_age)
    if spy_age < 12:
        print ' Too young to be an agent .....sorry'
        exit()
    if spy_age > 50:
        print ' You need to retire now ....Goodbye '
        exit()

    # ask the user about the rating and greet him accordingly
    spy_rating = float(raw_input('what is your spy rating '))
    if spy_rating > 4.7:
        print 'You are one of our special agengts .....We are lucky to have you'
    elif spy_rating > 3.5 and spy_rating <= 4.7:
        print 'You are one of the best agents we have '
    elif spy_rating < 3.5 and spy_rating > 2.7:
        print 'Welcome Agent .....you have a lot to prove'
    # show the spy details if he wants to stay online
    spy_is_online = True
    spy_stat = raw_input('do you want to stay online y/n')

    if (spy_stat.lower() == 'y'):
        spy_is_online = True
        print 'You are now Online .....'
        print 'Welcome ', spy_name, ' \n  Your details \n', 'Age- ', spy_age, '\nRating-', spy_rating
    # if not he can log off
    else:
        spy_is_online = False
        print 'Goodbye ....we will see you soon ...'
    return spy_name,spy_rating,spy_age

#method to update the status of the spy
def status_update(status):
    #print the current status
    print 'Status : ' , status
    if (status)==None:
        print 'status is empty'

    ch=raw_input('Do you want to update your status y/n')
    if ch.lower()=='y':
        ch=int(raw_input('1.Add a new status\n 2.Choose from an old one \n'))
        if ch==1:
            #adding a new status to be entered by the user e
            new_status=raw_input('New status: ')
            while len(new_status)==0:
                print 'Empty status !!!'

            status=new_status
            #using the append method to update the list of statuses
            status_list.append(new_status)
        elif ch==2 :
            i=1
            #using for loop to print the list of all the statuses entered by user in the past
            for temp in status_list:
                print i,'.', temp
                i=i+1
             #upodating status from the previous record of the statuses
            select=int(raw_input('choose the status you want to set'))
            status=status_list[select-1]
        print 'Updated Status: ',status
    else :
        print 'Back to main menu'
     #returning the new status so that it can be updated in the main app
    return status

def friend_list():
    temp_friend={
        'name':''
        ,'age':'',
        'rating':'',
        'is_online':'True',
        'chats':[]
    }

    print 'Friend List \n You have ',len(friends),' friends'
    ch=int(raw_input( '\n what would you like to do \n 1. View Friend list \n 2. Add a new friend '))

    if ch==1:
        i=1
        print'  Name \t\t    Age   Rating '
        for temp_friend in friends:
            print i,'.',temp_friend['name'] , '\t  ',temp_friend['age'],'\t  ',temp_friend['rating']
            i=i+1
    else :
        add_friend()


def add_friend():
        new_friend={
            'name':'',
            'age':'',
             'rating':'',
            'is_online':'True',
            'chats':[]
        }
        print 'Add the details of the friend'
        while len(new_friend['name'])==0:
            new_friend['name']=raw_input("Name of the friend")
            #friend_list.append(friend['name'])
       # while len(['age']) == 0:
            new_friend['age']=int(raw_input('Age of the friend'))
            #friend_age.append(age)

            new_friend['rating'] =float(raw_input('Spy rating of the friend'))
            #friend_rating.append(rating)
        print "Friend's data has been succesfully upated"
        friends.append(new_friend)

def select_friend():
    print 'Select from the friend list to whom you want to send a message '
    print 'Friend List \n You have ', len(friends), ' friends'
    temp_friend = {
        'name': ''
        , 'age': '',
        'rating': '',
        'chats':[]
    }

    i = 1
    print'  Name \t\t    Age   Rating '
    for temp_friend in friends:
            print i, '.', temp_friend['name'], '\t  ', temp_friend['age'], '\t  ', temp_friend['rating']
            i = i + 1
    index= int(raw_input( ' Select the friend whom you want to send a message '))
    return index-1
def send_message(index):
    text=raw_input('Enter the message you want to send')
    input=raw_input('select the image for encoding')
    output='output.jpg'
    Steganography.encode(input,output,text)
    temp_friend={
        'chats':[]
    }
    temp_friend=friends[index]
    temp_friend['chats'].append(output)
    print 'the message has been sent to ',temp_friend['name']
