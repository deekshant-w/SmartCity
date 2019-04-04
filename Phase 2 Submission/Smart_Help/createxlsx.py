import pandas as pd
from pandas import ExcelWriter          #-> et-xmlfile , openpyxl
from pandas import ExcelFile
import numpy as np
import os

#dt is the data to input and name is the name of the file the data is being written
def create_excel(dt,name):
    writer = ExcelWriter(name)  #creates an instance to write data
    dt.to_excel(writer, sheet_name='Sheet1')
    writer.save()

#function to check wether the given excel file exists
#and if no then create that file with initial data
#of dt and store in filename name
def new_excel(dt,name):
    if(not os.path.isfile(name)):
        create_excel(dt,name)


#sample data for trial run
"""data = pd.DataFrame([],[],["FName","SName","gender","DOB","phone","email","address","UID","password"])
create_excel(data,'daat')
print(data)"""


#smart.help.it.eve@gmail.com
#smarthelp@2019
