#This code is made by Quessts and is credited to Quessts. Kindly give credit before using it.
import sqlite3
import time
import sys

class bcolors:
	Red = '\033[91m'
	Green = '\033[92m'
	Blue = '\033[94m'
	Magenta = '\033[95m'

with sqlite3.connect('accounts.db') as db:
    cursor = db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS user(
userID INTEGER PRIMARY KEY,
username VARCHAR(20) NOT NULL,
firstname VARCHAR(20) NOT NULL,
lastname VARCHAR(20) NOT NULL,
password VARCHAR(20) NOT NULL);
''')


db.commit()

cursor.execute('SELECT * FROM user')
print(cursor.fetchall())

def login():
    while True:
        username = input(bcolors.Blue + 'Enter username: ')
        password = input('Enter password: ')
        with sqlite3.connect('accounts.db') as db:
            cursor = db.cursor()
        find_user = ('SELECT * FROM user WHERE username = ? AND password = ?')
        cursor.execute(find_user,[(username),(password)])
        results = cursor.fetchall()

        if results:
            for i in results:
                print('Welcome '+i[2])
            break

        else:
            print('Invalid username or password')
            again = input('Do you want to try again(y/n): ')
            if again.lower() == 'n':
                print('GoodBye')
                time.sleep(1)
                break


def newUser():
    found = 0
    while found ==0:
        username = input(bcolors.Green + 'Please enter a username: ')
        with sqlite3.connect('accounts.db') as db:
            cursor = db.cursor()
        findUser = ('SELECT * FROM user WHERE username = ?')
        cursor.execute(findUser,[(username)])

        if cursor.fetchall():
            print('Username Unavailabe. Please try again')
        else:
            found = 1
    firstname = input('Enter your first name: ')
    lastname = input('Enter your last name: ')
    password = input('Please enter your password: ')
    password1 = input('Please reenter your password: ')
    while password !=password1:
        print("Your password doesn't match. Please try again")
        password = input('Please enter your password: ')
        password1 = input('Please reenter your password: ')
    insertData = '''INSERT INTO user(username,firstname,lastname,password)
    VALUES(?,?,?,?)'''
    cursor.execute(insertData,[(username),(firstname),(lastname),(password)])
    db.commit()


def menu():
    while True:
        print('Welcome to Quessts Program. For more subscribe to my YouTube channel https://YouTube.com/Quessts')
        menu = (bcolors.Magenta + '''1- Create New User
2- Log in
3- Exit
> ''')

        userchoice = input(menu)

        if userchoice == '1':
            newUser()

        elif userchoice == '2':
            login()

        elif userchoice =='3':
            print(bcolors.Red + 'GoodBye')
            sys.exit()

        else:
            print('Command not recognised')

menu()
