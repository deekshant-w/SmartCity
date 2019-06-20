import pandas as pd
import os
from createxlsx import *
import json
import datetime

#file containing data for after login is sucessful
FILE_NAME = "final.xlsx"
database_template = pd.DataFrame([],[],["UID","data"]).set_index(["UID"])
database_template.loc["admin"] = {"admin":{"data":"admin","status":"pending"}}

#function for new inputs
#no returns its always sucessful
def new_entry(uid,inp):
    new_excel(database_template,FILE_NAME)
    handle = pd.read_excel(FILE_NAME,index_col="UID")
    users = handle.index
    if(uid in users):
        old_data = handle.loc[uid]["data"]                  #reads old data
        old_data = old_data.replace("\'","\"")              #replaces ' with "
        old_data = json.loads(old_data)                     #reads string converts to dict
        #stamp = date+time unique id
        hash = str(datetime.datetime.now().date()) + "+" + str(str(datetime.datetime.now().time()))
        #data is stored in the form-
        #excel file -> uid -> data column -> dict(explained below)
        #{datetime stamp : {data:" ",status:" "} , {}}
        old_data[hash] = {"data":inp,"status":"pending"}
        handle.loc[uid]["data"] = old_data
    else:
        hash = str(datetime.datetime.now().date()) + "+" + str(str(datetime.datetime.now().time()))
        temp = dict()
        temp[hash] = {"data":inp,"status":"pending"}
        handle.loc[uid] = [temp]
    create_excel(handle,FILE_NAME)

#new_entry("dkw","34sercdf b65 rfghb tyughbjn")

#function to check previous entries
#sucessful = (1,data in dictionary form as it was stored, see above)
#fail = (0,"No record found")
def old_entry(uid):
    new_excel(database_template,FILE_NAME)
    handle = pd.read_excel(FILE_NAME,index_col="UID")
    users = handle.index
    if(uid in users):
        temp = (handle.loc[uid]["data"])
        temp = str(temp)
        temp = temp.replace("\'","\"")
        temp = json.loads(temp)
        return (1,temp)
    else:
        return (0,"No record found")
#print((old_entry("dk")))
