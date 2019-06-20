# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 13:07:01 2019

root < topcanvas full < toplvlhomepage  half< buttons in frame1

@author: Nitesh
"""
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from entrylevel import sign_up,log_in
from tkinter import messagebox
#from tkinter import filedialog
from dkmail import mail
from userlevel import new_entry
#from dkfront import main_front
import pandas as pd
import os
from createxlsx import *
from flask import Flask,render_template,request
#from userlevel import old_entry
import webbrowser
import json
import datetime

FILE_NAME = "final.xlsx"
database_template = pd.DataFrame([],[],["UID","data"]).set_index(["UID"])
database_template.loc["admin"] = {"admin":{"data":"admin","status":"pending"}}

"""app = Flask(__name__)
    @app.route("/nerec")
    def nope():
    	return render_template("no_records.html")
    @app.route("/rec")
        def yep():
            cleandata = htmldata(handle[1])
            return render_template("details.html",data = cleandata)
    @app.route('/shutdown') #methods=['POST'])
    def shutdown():
        shutdown_server()
        
        return 'Server shutting down...'
    if __name__ == '__main__':
        print("Nitesh")
        webbrowser.open("http://127.0.0.1:5000/")
        app.run(debug=True)"""


root = tk.Tk()

global useratthetime;
global message;
global toplvlmainpage;
global toplvlhelppage;
global toplvlprevios;
global toplvlhomepage
global toplvlprevios;
global toplvllogin;
global Fname;
global Sname;
global email;
global passwordass;
global dob_date;
global dob_month;
global dob_year;
global frame1;
global topcanvas;
global uid,password;


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



bgimg = Image.open("8.png")
bgimg = bgimg.resize((1024,660),Image.ANTIALIAS)
bgimg = ImageTk.PhotoImage(bgimg)

bgimg2 = Image.open("1.jpg")
bgimg2 = bgimg2.resize((512,660),Image.ANTIALIAS)
bgimg2 = ImageTk.PhotoImage(bgimg2)

style = ttk.Style()
style.configure("TButton", font="Arial 15", padding =10)
style.configure("TEntry", font="Arial 15", padding = 9)
style.configure("TCombobox", font="Arial 15", padding = 10)
style.configure("TRadiobutton", font="Arial 9", padding = 9)



def inilogin():
    global topcanvas
    global toplvlhomepage;
    global toplvllogin
    toplvlhomepage.destroy()
    createlogin()
    
    
    
def inisignup():
    global toplvlhomepage;
    global toplvlsignup;
    toplvlhomepage.destroy()
    createsignup()
    
def inimainpage():
    global toplvllogin;
    try:
        toplvllogin.destroy()
    except: pass
    finally:
        createlvlmainpage()





#HOME PAGE

root.geometry("1024x660")
root.resizable(width=False, height=False)
root.title("Smart Help")
root.configure()

topcanvas = tk.Canvas(root, width= 1024, height = 660)
topcanvas.create_image(0,0,anchor = tk.NW,image = bgimg)





def createhomepage():
    global useratthetime;
    global message;
    global toplvlmainpage;
    global toplvlhelppage;
    global toplvlprevios;
    global toplvlhomepage
    global toplvlprevios;
    global toplvllogin;
    global Fname;
    global Sname;
    global email;
    global passwordass;
    global dob_date;
    global dob_month;
    global dob_year;
    global frame1;
    global topcanvas;
    global uid,password;
    toplvlhomepage = tk.Canvas(topcanvas,width = 512, height = 660)

    toplvlhomepage.create_image(0,0,anchor = tk.NW,image = bgimg2)
    topcanvas.create_window((256,0),window = toplvlhomepage,anchor = tk.NW)
    
    
    
    #title = ttk.Label(toplvlhomepage, text="SMART HELP", font=("Tahoma", 40, 'bold'), width=300, anchor = tk.NW)
    toplvlhomepage.create_text(256,50,anchor = tk.N,font = 'Tohama 60 bold',text = "Smart",fill = 'black')
    toplvlhomepage.create_text(256,130,anchor = tk.N,font = 'Tohama 60 bold',text = "Help",fill = 'black')
    #create_window((256,2),window = title,anchor = tk.N, width=505)
    #title.configure(anchor="center")
    
    
    frame1 = tk.Frame(toplvlhomepage)
    button_Login = tk.Button(frame1 , text="Login", command= inilogin, bg = "#f24245",fg='white',relief='flat',width=18,height = 2, font =("Calibri", 20, 'bold'), activebackground = "#CE3312")
    
    button_signup = tk.Button(frame1 , text="SignUp", command= inisignup, bg = "#16a39d",fg='white',relief='flat',width=18,height = 2, font =("Calibri", 20, 'bold'), activebackground = "#107f79")
    button_Login.grid(row = 1,column = 2)
    button_signup.grid(row = 1,column = 1)
    
    
    toplvlhomepage.create_window((256,660),window = frame1,anchor = tk.S,width = 512)


# SIGNUP
def createsignup():
    global useratthetime;
    global message;
    global toplvlmainpage;
    global toplvlhelppage;
    global toplvlprevios;
    global toplvlhomepage
    global toplvlprevios;
    global toplvllogin;
    global Fname;
    global Sname;
    global email;
    global passwordass;
    global dob_date;
    global dob_month;
    global dob_year;
    global frame1;
    global toplvlsignup;
    global gender;
    global address;
    global phone;
    global topcanvas;
    global uid,password;
    toplvlsignup = tk.Canvas(topcanvas,width = 512, height = 660, bg = 'black')
    toplvlsignup.create_image(0,0,anchor = tk.NW,image = bgimg2)
    toplvlsignup.create_text(256,5,anchor = tk.N,font = 'Ethon 40 bold',text = "SIGN UP")
    toplvlsignup.create_text(180,110,anchor = tk.NE,font = 'Ethon 20 bold',text = "First Name")
    
    Fname = tk.StringVar()
    first_name_entry = ttk.Entry(toplvlsignup, textvariable=Fname, width=70)
    toplvlsignup.create_window((480,110),window =first_name_entry,anchor = tk.NE, width=256)
    
    
    toplvlsignup.create_text(180,170,anchor = tk.NE,font = 'Ethon 20 bold',text = "Last Name")
    Sname = tk.StringVar()
    last_name_entry = ttk.Entry(toplvlsignup, textvariable=Sname, width=70,)
    toplvlsignup.create_window((480,170),window =last_name_entry,anchor = tk.NE, width=256)
    
    
    
    toplvlsignup.create_text(180,230,anchor = tk.NE,font = 'Ethon 20 bold',text = "Password")
    passwordass = tk.StringVar()
    password_entry = ttk.Entry(toplvlsignup, textvariable=passwordass, width=70, show="*")
    toplvlsignup.create_window((480,230),window =password_entry,anchor = tk.NE, width=256)
    
    
    toplvlsignup.create_text(180,290,anchor = tk.NE,font = 'Ethon 20 bold',text = "Date of Birth")
    dob_date = tk.StringVar()
    dob_date.set("1")
    dob_date_choices = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
    dob_month_dropdown=ttk.Combobox(toplvlsignup,textvariable=dob_date, values=dob_date_choices)
    toplvlsignup.create_window((270,290),window =dob_month_dropdown,anchor = tk.N, width=80)
    
    dob_month = tk.StringVar()
    dob_month.set("January")
    dob_month_choices = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    dob_month_dropdown=ttk.Combobox(toplvlsignup,textvariable=dob_month, values=dob_month_choices)
    toplvlsignup.create_window((355,290),window =dob_month_dropdown,anchor = tk.N, width=80)
    
    dob_year = tk.StringVar()
    dob_year.set("1971")
    dob_year_choices = [" 1901 "," 1902 "," 1903 "," 1904 "," 1905 "," 1906 "," 1907 "," 1908 "," 1909 "," 1910 "," 1911 "," 1912 "," 1913 "," 1914 "," 1915 "," 1916 "," 1917 "," 1918 "," 1919 "," 1920 ",
    " 1921 "," 1922 "," 1923 "," 1924 "," 1925 "," 1926 "," 1927 "," 1928 "," 1929 "," 1930 "," 1931 "," 1932 "," 1933 "," 1934 "," 1935 "," 1936 "," 1937 "," 1938 "," 1939 "," 1940 ",
    " 1941 "," 1942 "," 1943 "," 1944 "," 1945 "," 1946 "," 1947 "," 1948 "," 1949 "," 1950 "," 1951 "," 1952 "," 1953 "," 1954 "," 1955 "," 1956 "," 1957 "," 1958 "," 1959 "," 1960 ",
    " 1961 "," 1962 "," 1963 "," 1964 "," 1965 "," 1966 "," 1967 "," 1968 "," 1969 "," 1970 "," 1971 "," 1972 "," 1973 "," 1974 "," 1975 "," 1976 "," 1977 "," 1978 "," 1979 "," 1980 ",
    " 1981 "," 1982 "," 1983 "," 1984 "," 1985 "," 1986 "," 1987 "," 1988 "," 1989 "," 1990 "," 1991 "," 1992 "," 1993 "," 1994 "," 1995 "," 1996 "," 1997 "," 1998 "," 1999 "," 2000 ",
    " 2001 "," 2002 "," 2003 "," 2004 "," 2005 "," 2006 "," 2007 "," 2008 "," 2009 "," 2010 "," 2011 "," 2012 "," 2013 "," 2014 "," 2015 "," 2016 "," 2017 "," 2018 "," 2019 "]
    dob_year_dropdown=ttk.Combobox(toplvlsignup,textvariable=dob_year, values=dob_year_choices)
    toplvlsignup.create_window((440,290),window =dob_year_dropdown,anchor = tk.N, width=80)
    
    
    
    toplvlsignup.create_text(180,350,anchor = tk.NE,font = 'Ethon 20 bold',text = "Gender")
    gender=tk.StringVar()
    gender.set('O')
    rb1 = ttk.Radiobutton(toplvlsignup, text='Male', variable=gender, value='M')
    rb2 = ttk.Radiobutton(toplvlsignup, text='Female', variable=gender, value='F')
    rb3 = ttk.Radiobutton(toplvlsignup, text='Other', variable=gender, value='O')
    
    toplvlsignup.create_window((305,350),window =rb1,anchor = tk.NE, width=80)
    toplvlsignup.create_window((395,350),window =rb2,anchor = tk.NE, width=80)
    toplvlsignup.create_window((485,350),window =rb3,anchor = tk.NE, width=80)
    
    
    
    toplvlsignup.create_text(180,410,anchor = tk.NE,font = 'Ethon 20 bold',text = "Phone No.")
    phone = tk.StringVar()
    phone_number = ttk.Entry(toplvlsignup, textvariable=phone, width=70)
    toplvlsignup.create_window((480,410),window =phone_number,anchor = tk.NE, width=256)
    
    
    
    
    toplvlsignup.create_text(180,470,anchor = tk.NE,font = 'Ethon 20 bold',text = "Email ID")
    email = tk.StringVar()
    email_entry = ttk.Entry(toplvlsignup, textvariable=email, width=70)
    toplvlsignup.create_window((480,470),window =email_entry,anchor = tk.NE, width=256)
    
    
    
    toplvlsignup.create_text(180,530,anchor = tk.NE,font = 'Ethon 20 bold',text = "Address")
    address = tk.StringVar()
    address_entry = ttk.Entry(toplvlsignup, textvariable=address, width=70)
    toplvlsignup.create_window((480,530),window =address_entry,anchor = tk.NE, width=256)

    frame1 = tk.Frame(toplvlsignup)
    button_continue = ttk.Button(frame1 , text="Sign Up", command= lambda: nsign_up())
    
    button_continue.pack()
    
    toplvlsignup.create_window((256,600),window = frame1,anchor = tk.N,width = 140)
    topcanvas.create_window((256,0),window = toplvlsignup,anchor = tk.NW)
def nsign_up():
    global useratthetime;
    global message;
    global toplvlmainpage;
    global toplvlhelppage;
    global toplvlprevios;
    global toplvlhomepage
    global toplvlprevios;
    global toplvllogin;
    global Fname;
    global Sname;
    global email;
    global passwordass;
    global dob_date;
    global dob_month;
    global dob_year;
    global frame1;
    global toplvlsignup;
    global gender;
    global address;
    global phone;
    global topcanvas;
    global uid,password;
    dbt=(dob_date.get()+dob_month.get()+dob_year.get())
    ttt = {'FName': Fname.get(),'SName': Sname.get(),"DOB": dbt,"gender":gender.get(),"phone":phone.get(),"email":email.get(),"address":address.get(),"password": passwordass.get()}
    x = sign_up(ttt)
    if x[0]==0:
        messagebox.showinfo("Information","SignUp Successful\nYour Unique ID id is {}\nCheck your mail for your mail for confirmation".format(x[1]))
        mail(email.get(),"Your account have been created successfully.\nYour USER ID is {} and password is {}.\nThank You for using Smart Help".format(x[1],passwordass.get()))
        inilogin()
    else:
        messagebox.showerror("Error",x[1])
#SIGNUP ENDS
def nlogin():
    global useratthetime;
    global message;
    global toplvlmainpage;
    global toplvlhelppage;
    global toplvlprevios;
    global toplvlhomepage;
    global toplvlsignup;
    global toplvlprevios;
    global toplvllogin;
    global Fname;
    global Sname;
    global email;
    global passwordass;
    global dob_date;
    global dob_month;
    global dob_year;
    global frame1;
    global topcanvas;
    global uid,password;
    x = log_in(uid.get(),password.get())
    if x[0] == 1:
        messagebox.showinfo("Information","Login Successful")
        useratthetime = x[1].name
        inimainpage()
    else:
        messagebox.showerror("Error","Check your password again, Please go to SignUp if you are a new user")
#LOGIN
        
def createlogin():
    global useratthetime;
    global message;
    global toplvlmainpage;
    global toplvlhelppage;
    global toplvlprevios;
    global toplvlhomepage
    global toplvlprevios;
    global toplvllogin;
    global toplvlsignup;
    global Fname;
    global Sname;
    global email;
    global passwordass;
    global dob_date;
    global dob_month;
    global dob_year;
    global frame1;
    global topcanvas;
    global uid,password;
    toplvllogin = tk.Canvas(topcanvas,width = 512, height = 660, bg = 'black')
    toplvllogin.create_image(0,0,anchor = tk.NW,image = bgimg2)
    toplvllogin.create_text(256,5,anchor = tk.N,font = 'Ethon 40 bold',text = "LOG IN")
    
    
    toplvllogin.create_text(180,200,anchor = tk.NE,font = 'Ethon 20 bold',text = "Unique ID")
    uid = tk.StringVar()
    uid_entry = ttk.Entry(toplvllogin, textvariable=uid, width=70)
    toplvllogin.create_window((480,200),window =uid_entry,anchor = tk.NE, width=256)
    
    
    toplvllogin.create_text(180,260,anchor = tk.NE,font = 'Ethon 20 bold',text = "Password")
    password = tk.StringVar()
    password_entry = ttk.Entry(toplvllogin, textvariable=password, width=70, show="*")
    toplvllogin.create_window((480,260),window =password_entry,anchor = tk.NE, width=256)





        





    frame1 = tk.Frame(toplvllogin)
    button_login = ttk.Button(frame1 , text="Log In", command= nlogin)
    button_login.pack()
    
    toplvllogin.create_window((256,340),window = frame1,anchor = tk.N,width = 140)
    topcanvas.create_window((256,0),window = toplvllogin,anchor = tk.NW)
    

#LOGIN ENDS
def needhelp():
    global useratthetime;
    global message;
    global toplvlmainpage;
    global toplvlhelppage;
    global toplvlprevios;
    global toplvlhomepage
    global toplvlprevios;
    global toplvllogin;
    global Fname;
    global Sname;
    global toplvlsignup;
    global email;
    global passwordass;
    global dob_date;
    global dob_month;
    global dob_year;
    global frame1;
    global topcanvas;
    global uid,password;
    try :
        toplvllogin.destoy()
    except: pass
    finally:
        createlvlhelppage()

def prevcases():
    global message;
    global toplvlmainpage;
    global toplvlhelppage;
    global toplvlprevios;
    global toplvlhomepage
    global toplvlprevios;
    global toplvllogin;
    global Fname;
    global Sname;
    global email;
    global passwordass;
    global dob_date;
    global dob_month;
    global dob_year;
    global frame1;
    global useratthetime;
    global toplvlsignup;
    global topcanvas;
    global uid,password;
    app = Flask(__name__)
    handle = old_entry(uid.get())
    if(handle[0]==0):
        @app.route("/")
        def nope():
            return render_template("no_records.html")
    else:
        @app.route("/")
        def yep():
            cleandata = htmldata(handle[1])
            return render_template("details.html",data = cleandata)
    @app.route('/shutdown') #methods=['POST'])
    def shutdown():
        shutdown_server()
        
        return 'Server shutting down...'
    if __name__ == '__main__':
        print("Nitesh")
        webbrowser.open("http://127.0.0.1:5000/")
        app.run(debug=True,use_reloader=False)
#    toplvlsignup.create_window((256,600),window = frame1,anchor = tk.N,width = 140)
    """
    
    """
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
def htmldata(dt):
    temp = []
    for x in dt:
        t = dt[x]
        tt = x.split("+")
        t["date"] = tt[0]
        t["time"] = tt[1]
        t["stamp"] = x
        temp.append(t)
    return temp

def main_front(uid):
    app = Flask(__name__)
    handle = old_entry(uid)
    print(handle)
    if(handle[0]==0):
        @app.route("/")
        def nope():
            return render_template("no_records.html")
    else:
        @app.route("/")
        def yep():
            cleandata = htmldata(handle[1])
            return render_template("details.html",data = cleandata)
    @app.route('/shutdown') #methods=['POST'])
    def shutdown():
        shutdown_server()
        
        return 'Server shutting down...'
    if __name__ == '__main__':
        print("Nitesh")
        webbrowser.open("http://127.0.0.1:5000/")
        app.run(debug=True)
        """
        """
#MainPage
def createlvlmainpage():
    global useratthetime;
    global message;
    global toplvlmainpage;
    global toplvlhelppage;
    global toplvlprevios;
    global toplvlsignup;
    global toplvlhomepage
    global toplvlprevios;
    global toplvllogin;
    global Fname;
    global Sname;
    global email;
    global passwordass;
    global dob_date;
    global dob_month;
    global dob_year;
    global frame1;
    global topcanvas;
    global uid,password;
    toplvlmainpage = tk.Canvas(topcanvas,width = 512, height = 660)
    toplvlmainpage.create_image(0,0,anchor = tk.NW,image = bgimg2)
    toplvlmainpage.create_text(256,5,anchor = tk.N,font = 'Ethon 40 bold',text = "How can we help !!",fill = "black")
    
    
        
    
    
    frame1 = tk.Frame(toplvlmainpage)
    button_need_help = ttk.Button(frame1 , text="Need Help", command= needhelp)
    button_need_help.pack()
    toplvlmainpage.create_window((256,256),window = frame1,anchor = tk.N,width = 150)
    
    
    frame2 = tk.Frame(toplvlmainpage)
    button_previous_cases = ttk.Button(frame2 , text="Previous Cases", command= prevcases)
    button_previous_cases.pack()
    toplvlmainpage.create_window((256,512),window = frame2,anchor = tk.N,width = 170)
    topcanvas.create_window((256,0),window = toplvlmainpage,anchor = tk.NW)
    

#mainpage ends
def submit():
    global useratthetime;
    global message;
    global toplvlmainpage;
    global toplvlhelppage;
    global toplvlprevios;
    global toplvlhomepage
    global toplvlprevios;
    global toplvllogin;
    global Fname;
    global toplvlsignup;
    global Sname;
    global email;
    global passwordass;
    global dob_date;
    global dob_month;
    global dob_year;
    global frame1;
    global topcanvas;
    global uid,password;
    global heading;
    new_entry(useratthetime,heading.get()+" -> "+message.get())
    try :
        toplvlhelppage.destroy()
    except: pass
    finally:
        inimainpage()
    messagebox.showinfo("Information","Your query have been recorded!!")
#Help Page

def createlvlhelppage():
    global heading;
    global useratthetime;
    global message;
    global toplvlmainpage;
    global toplvlhelppage;
    global toplvlprevios;
    global toplvlhomepage
    global toplvlprevios;
    global toplvllogin;
    global Fname;
    global Sname;
    global email;
    global passwordass;
    global dob_date;
    global dob_month;
    global dob_year;
    global toplvlsignup;
    global frame1;
    global topcanvas;
    global uid,password;
    toplvlhelppage = tk.Canvas(topcanvas,width = 512, height = 660, bg = 'black')
    toplvlhelppage.create_image(0,0,anchor = tk.NW,image = bgimg2)
    toplvlhelppage.create_text(256,8,anchor = tk.N,font = 'Tohama 40 bold',text = "How can we help?")
    
    
    
    #Heading
    toplvlhelppage.create_text(250,110,anchor = tk.N,font = 'Ethon 20 bold',text = "Regarding")
    
    
    
    heading = tk.StringVar()
    # first_name_entry = ttk.Entry(toplvlhelppage, textvariable=Fname, width=70)
    heading_entry = ttk.Entry(toplvlhelppage, textvariable=heading , width=100)
    
    toplvlhelppage.create_window((500,160),window =heading_entry,anchor = tk.NE, width=490)
    
    
    toplvlhelppage.create_text(250,250,anchor = tk.N,font = 'Ethon 20 bold',text = "Query")
    
    #style.configure("TEntry", font="Arial 80", padding = 10)
    
    message = tk.StringVar()
    # first_name_entry = ttk.Entry(toplvl, textvariable=Fname, width=70)
    
    
    
    message_entry = tk.Entry(toplvlhelppage,textvariable = message)
    toplvlhelppage.create_window((500,300),window =message_entry,anchor = tk.NE, width=490, height = 280)
    
    
    
    
    frame1 = tk.Frame(toplvlhelppage)
    button_continue = ttk.Button(frame1 , text="Submit", command= submit)
    
    button_continue.pack()
    toplvlhelppage.create_window((256,600),window = frame1, anchor = tk.N,width = 140)
    topcanvas.create_window((256,0),window = toplvlhelppage,anchor = tk.NW)


#help ends
def prevclose():
    global useratthetime;
    global message;
    global toplvlmainpage;
    global toplvlhelppage;
    global toplvlprevios;
    global toplvlhomepage
    global toplvlprevios;
    global toplvllogin;
    global Fname;
    global Sname;
    global email;
    global passwordass;
    global toplvlsignup;
    global dob_date;
    global dob_month;
    global dob_year;
    global frame1;
    global topcanvas;
    global uid,password;
    toplvlprevios.destroy()
#Previous Records

    

    toplvlprevios = tk.Canvas(topcanvas,width = 512, height = 660, bg = 'black')
    toplvlprevios.create_image(0,0,anchor = tk.NW,image = bgimg2)
    toplvlprevios.create_text(256,8,anchor = tk.N,font = 'Tohama 40 bold',text = "Previous Cases")
    
    frameprev = tk.Frame(toplvlprevios)
    button_continue = ttk.Button(frameprev , text="BACK", command= lambda: prevclose())
    
    button_continue.pack()
    toplvlhelppage.create_window((256,600),window = frameprev,anchor = tk.N,width = 140)
#previos records close

createhomepage()




topcanvas.pack()











root.mainloop()


