#Mini Lab
import re

emailList = []
passwordList = []
tries = 3
def displayMenu():
    print("Enter Sign In or Sign Up")
    check = input()
    return check

def enterInfo():
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    return email, password


def validatePassword(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    return True

def readFile():
    with open("emails_passwords.txt") as f:
        while True:
            line = f.readline()
            if not line:
                break
            x = line.strip().split(" ")
            emailList.append(x[0])
            passwordList.append(x[1])

def writeFile(signupemail, signuppassword):
    with open("emails_passwords.txt", "a") as f:
        f.write(f"{signupemail} {signuppassword} \n")
        emailList.append(signupemail)
        passwordList.append(signuppassword)


program = True
while program == True:
    option = displayMenu()
    

    readFile()

    login = False
    
    if option.upper() == "SIGN IN":
        while tries > 0:
            email, password = enterInfo()
            emailInList = False
            passwordInList = False
            for x in emailList:
                if x == email:
                    emailInList = True

            for x in passwordList:
                if x == password:
                    passwordInList = True
                
            if emailInList == True and passwordInList == True:
                login = True   
                break
            else:
                tries -= 1
                print(f"Invalid email or password. Try Again you have {tries} attempts left")
                
        else:
            print("Too many trys. Your not allow access anymore")
            program = False
    
    elif option.upper() == "SIGN UP":
        email, password = enterInfo()
        while True:
            if validatePassword(password):
                writeFile(email, password)
                print("Account created")
                break
            else:
                print("Password was to Weak, try again")
                print("Password must be 8 characters long, include a number, upper and lower letter ")
                password = input("")
    
    if login == True:  
        print(f"Welcome {email}")
        break
    
