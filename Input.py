# name = input("Please enter your name : ")
# age = input("Please enter your age : ")
# bday = input("What month was your birthday : ")
#
# print("Hello " + name)
# print("You are " + age + "years old and were born in the month of " + bday)


ilogin = ("")
ipass = ("")

def displayWelcome():
    print("Welcome to the Xyz, Inc. SSH server")
    print("")


def getUserLogin():
    return input("Please enter your login name : ")


def getUserPass():
    return input("Please enter your password : ")

def displayLoginCred(login, password):
    print("Login : " + login)
    print("Pass : " + password)

displayWelcome()
ilogin = getUserLogin()
ipass = getUserPass()
displayLoginCred(ilogin, ipass)
