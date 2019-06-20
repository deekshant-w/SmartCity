from createxlsx import *
import pandas as pd   #-> xlrd
import re
import random
import string

FILE_NAME = "test.xlsx"         #file containg basic information
database_template = pd.DataFrame([],[],["FName","SName","gender","DOB","phone","email","address","UID","password"]).set_index(["UID"])
database_template.loc["admin"] = ["admin","admin","admin","admin","admin","admin","admin","admin"]


#function to check wether the inputs were correct
#function returns [0,""] on sucessful completion
#function returns [>0,error] if somthing went wrong
def sign_up_check(d):
    error = ""
    eror = 0
    if(d["FName"]==""):
        eror += 1

    if(d["phone"]==""):
        error+="Phone Number cannot be empty\n"
        eror += 1
        error+="First Name cannot be empty\n"
        eror += 1

    if(d["SName"]==""):
        error+="Last Name cannot be empty\n"

    try:
        temp = int(d["phone"])
    except:
        error+="Phone Number cannot contain a charecter\n"
        eror += 1

    if(len(d["phone"])!=10):
        error+="Phone Number should be of 10 digits\n"
        eror += 1

    if(d["email"]==""):
        error+="Email id cannot be empty\n"
        eror += 1

    try:
        temp = re.match('\S+@\S+[.][c][o][m]',d["email"])[0]
    except:
        error+="Invalid Email Id\n"
        eror += 1

    if(d["address"]==""):
        error+="Address cannot be empty\n"
        eror += 1

    if(len(d["password"])<6):
        error+="Password should of minimum 6 charecters\n"
        eror += 1

    return([eror,error])

def unique_uid():
    x = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
    return x

#function for signup processing
#function returns [0] on sucessful completion
#function returns [>0,error] in case of error
def sign_up(d):
    new_excel(database_template,FILE_NAME)              #checking for file existance
    data = pd.read_excel(FILE_NAME,index_col = "UID")   #reading database file
    inps = list(data.index)
    check = sign_up_check(d)
    UID = unique_uid()                                  #creating unique userids
    while UID in inps:
        UID = unique_uid()
    if(check[0]==0):
        data.loc[UID] = [d["FName"],d["SName"],d["gender"],d["DOB"],d["phone"],d["email"],d["address"],d["password"]]
        create_excel(data,FILE_NAME)
        return [0,UID]
    else:
        return check

#function for login process
#sucess = [1,userdetails as a pandas series]
#fail = [0]
def log_in(uid,password):
    new_excel(database_template,FILE_NAME)
    try:
        data = pd.read_excel(FILE_NAME,index_col = "UID")
        if(data.loc[uid]["password"]==password):
            return [1,data.loc[uid]]
        else:
            return [0]
    except KeyError:
        return [0]

#testing data
"""dt = {"FName":"deekhn","SName":"sd","gender":"M","DOB":"14.09.2000","phone":"8745989797","email":"d@d.com","address":"c7","password":"ddddsjh"}
print(log_in("admin","admin"))
print(sign_up(dt))"""
