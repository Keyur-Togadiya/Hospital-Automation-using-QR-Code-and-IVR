# import library 
import math, random
import vlc
from tkinter import *
import datetime
import time
from firebase import firebase
from tkinter import messagebox as ms
'from passengerDetailsGUI import *'
'from reservationGUI import *'
import sqlite3

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days = 1)
dtomorrow = today + datetime.timedelta(days = 2)

def generateOTP() : 

    digits = "0123456789"
    OTP = "" 
  

    for i in range(4) : 
        OTP += digits[math.floor(random.random() * 10)] 
  
    return OTP

con = sqlite3.connect('trial.db')
c = con.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS trial (Department CHAR(20), Date DATE, Time TIME, OTP INT)''')
c.execute('''DELETE FROM trial''')



FBConn = firebase.FirebaseApplication('https://vigourhealth-a34c1.firebaseio.com/', None)


flag=0
#main Class
class main:
    def __init__(self,master):
        # Window 
        self.master = master
        master.configure(background ="#ffffff", width=346, height=690)
            # Some Usefull variables
        self.username = StringVar()
        self.password = StringVar()
        self.otp = StringVar()
        self.cu = StringVar()
        #Create Widgets
        self.image13 = PhotoImage(file='logo1.png', height=140, width=140)
        self.image14 = PhotoImage(file='user.png', height=150, width=150)
        self.file1 = PhotoImage(file="10.png", height=30, width=120)
        self.widgets1()


    #Draw Widgets
    def widgets1(self):
        self.mainframe = Frame(self.master, bg='#ffffff', width=346, height=690)
        self.mainframe.pack(fill=BOTH)
        # 1st frame


        self.head1 = Label(self.mainframe, image=self.image13, bg="#ffffff", fg="#ffffff")
        self.head1.place(x=103, y=70)

        
        Label(self.mainframe,text = ' Enter OTP here :- ',font = ('',17),pady=4,padx=10, bg="#ffffff",fg="#fece2f").place(x=50, y=270)
        Entry(self.mainframe,textvariable = self.otp,font = ('',15), bg="#eceff1", fg="#fece2f").place(x=60, y=310)
                
        self.banswer = Button(self.mainframe,bg='#ffffff',image=self.file1, borderwidth=0,height=30, width=120, command = self.play)
        self.banswer.place(x=113, y=360)

        self.lking = Label(self.mainframe, text= " ", font=('Coda Regular', 35, 'italic'), bg="#ffffff",fg="#f0f").place(x=10, y=430)

    def play(self):
        with sqlite3.connect('trial.db') as db:
            c = db.cursor()

        # Find if Existing username and flight id exist if any take proper action
        find_data = ('SELECT * FROM trial WHERE OTP = ?')
        cursor = c.execute(find_data, [(self.otp.get())])
        apdetails=c.fetchall()
        res = FBConn.get('/IVR/', None)
        
        item = self.otp.get()
        for key in res.keys():
            if item in res[key]:
                c=key 
   
        self.lking0 = Label(self.mainframe, text= "Department : "+res[c][0], font=('Coda Regular', 12, 'italic'),bg="#ffffff", fg="#fece2f").place(x=20, y=430)
        self.lking1 = Label(self.mainframe, text= "Date : "+res[c][1], font=('Coda Regular', 12, 'italic'),bg="#ffffff", fg="#fece2f").place(x=20, y=450)
        self.lking2 = Label(self.mainframe, text= "Time : "+res[c][2], font=('Coda Regular', 12, 'italic'),bg="#ffffff", fg="#fece2f").place(x=20, y=470)
       
      
       
       
        

        
        
if __name__ == '__main__':
    #Create Object
    #and setup window
    root1 = Tk()
    root1.title('Vigour')
    #root.geometry('1366x768')
    #root1.state("zoomed")
    main(root1)
    root1.mainloop()        