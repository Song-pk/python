# name = input("Please enter your name : ")
# age = input("Please enter your age : ")
# bday = input("What month was your birthday : ")
#
# print("Hello " + name)
# print("You are " + age + "years old and were born in the month of " + bday)

password = ("s3cr3t")
ilogin = ("")
ipass = ("")

def displayWelcome():
    print("Welcome to the Xyz, Inc. SSH server")
    print("")


def getUserLogin():
    return input("root@127.0.0.1 : ")


def getUserPass():
    return input("Password : ")

def displayLoginCred(login, password):
    print("Login : " + login)
    print("Pass : " + passwrd)


def checkPassword(passwrd):
    global password
    if passwrd == password:
        return "true";
    else:
        return "false";


displayWelcome()
ilogin = getUserLogin()
ipass = getUserPass()


print(checkPassword(ipass));

# displayLoginCred(ilogin, ipass)
