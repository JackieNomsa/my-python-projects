
def register():
    name = input('Enter your name: ')
    email = input('Enter your email: ')
    password = input('Create password: ')
    confirm_password = input('Enter the same password to confirm: ')

    if password == confirm_password:
        with open('data.txt','a') as my_data:
            person = f'{name} {email} {password}'
            my_data.write(person)
            my_data.write('\n')
        print('you have been registered')
    else:
        print('that password does not match')
        register()


def login():
    name = input('Enter your name: ')
    password = input('Enter password: ')
    
    my_user = []
    with open('data.txt','r') as my_data:
        my_users = my_data.readlines()
        for i in my_users:
            my_user.append(i.strip('\n').split(' '))
        # print(my_user)
    for user in my_user:
        if name and password in user:
            print('login successful')
            havefun()
            break
    else:
        print('that name and password does not match')
        login()
            
        
def havefun():
    my_story = input('so what are you bloging about today? ')
    print('great lets get started')
    


answer = input('Do you have an accont (Yes or No): ')

if answer.lower() == 'yes':
    print('please login!')
    login()
else:
    print('please register')
    register()

