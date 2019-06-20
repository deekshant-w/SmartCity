import smtplib

#function to send an email from my gmail to given email Address using the below email and password`
#msg is the message being sent

my_mail = "smart.help.it.eve@gmail.com"
my_pass = "smarthelp@2019"


def mail(reciever,msg):
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)     #SMTP default gateway
        s.starttls()                                #start the server
        s.login(my_mail,my_pass)                    #login
        s.sendmail(my_mail,reciever,msg)            #sending
        s.quit()                                    #logout
    except:
        print("some error occured while sending the mail")
        pass

#trial data
"""mail("niteshks247@gmail.com","It worked")"""