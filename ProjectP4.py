#Thelma Valdez
#CIS 261 Progamming I
#WK9 Project Phase 4
from datetime import datetime

def Login():
        # read login information and store in a list
    UserFile = open("users.txt", "r")
    UserList = []
    UserName = input("Enter User Name: ")
    UserRole = "None"
    while True:
        UserDetail = UserFile.readline()
        if not UserDetail:
            return UserRole, UserName
        UserDetail = UserDetail.replace("\n") #remove carriage return from end of line
        UserList = UserDetail.split("|")
        if UserName == UserList[0]:
            UserRole = UserList[2] # user is valid, return role
            return UserRole, UserName


def 