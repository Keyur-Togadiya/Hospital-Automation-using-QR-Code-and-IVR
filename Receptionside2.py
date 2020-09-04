# import library 
import math, random
from tkinter import *
import datetime
import time
from firebase import firebase
from tkinter import messagebox as ms
import pyqrcode
import png
from pyqrcode import QRCode



today = datetime.date.today()
tomorrow = today + datetime.timedelta(days = 1)
past = today - datetime.timedelta(days = 1)



def generateOTP() : 
    digits = "0123456789"
    OTP = "" 
    for i in range(4) : 
        OTP += digits[math.floor(random.random() * 10)]   
    return OTP


# ======================================= Firebase ===========================================================================
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
        self.pname = StringVar()       
        self.pnumber = StringVar()
        self.pemail = StringVar()
        self.pdob = StringVar()
        self.pbloodgr = StringVar()
        self.pgender = StringVar()
        
        
        #Create Widgets
        self.image13 = PhotoImage(file='logo1.png', height=140, width=140)
        self.image14 = PhotoImage(file='user.png', height=150, width=150)
        self.file1 = PhotoImage(file="10.png", height=30, width=120)
        self.genqr = PhotoImage(file="genqr.png", height=42, width=42)
        self.details = PhotoImage(file="details.png", height=40, width=40)        
        self.widgets1()


    #Draw Widgets
    def widgets1(self):
        self.mainf = Frame(self.master, bg='#ffffff', width=346, height=690)
        self.mainf.pack(fill=BOTH)
        self.mainframe = Frame(self.mainf, bg='#ffffff', width=346, height=690)
        self.mainframe.pack(fill=BOTH)
        # 1st frame


        self.head1 = Label(self.mainframe, image=self.image13, bg="#ffffff", fg="#ffffff")
        self.head1.place(x=103, y=70)

        
        Label(self.mainframe,text = ' Enter OTP here :- ',font = ('',17),pady=4,padx=10, bg="#ffffff",fg="#fece2f").place(x=50, y=270)
        Entry(self.mainframe,textvariable = self.otp,font = ('',15), bg="#eceff1", fg="#fece2f").place(x=60, y=310)
                
        self.banswer = Button(self.mainframe,bg='#ffffff',image=self.file1, borderwidth=0,height=30, width=120, command = lambda: self.play())
        self.banswer.place(x=113, y=360)

        self.lking = Label(self.mainframe, text= " ", font=('Coda Regular', 35, 'italic'), bg="#ffffff",fg="#fece2f").place(x=10, y=430)

    def play(self):
        res = FBConn.get('/IVR/', None)
        item = self.otp.get()
        for key in res.keys():
            if item in res[key]:
                c=key 
            
        self.lking0 = Label(self.mainframe, text= "Department : "+res[c][0], font=('Coda Regular', 15, 'italic'),bg="#ffffff", fg="#fece2f").place(x=20, y=430)
        self.lking1 = Label(self.mainframe, text= "Date : "+res[c][1], font=('Coda Regular', 15, 'italic'),bg="#ffffff", fg="#fece2f").place(x=20, y=460)
        self.lking2 = Label(self.mainframe, text= "Time : "+res[c][2], font=('Coda Regular', 15, 'italic'),bg="#ffffff", fg="#fece2f").place(x=20, y=490)
                            
                            
        self.genrat = Button(self.mainframe, image=self.details, bd=0, bg='white', fg='white', command = lambda: self.qrgen())
        self.genrat.place(x=150, y=550)



    def qrgen(self):
        self.mainframe.destroy()
        self.laba = Label(self.mainf, bg="#ffffff", fg="#ffffff", width=346, height=690)
        self.laba.pack()
        self.lab2 = Label(self.laba,  bg="#ffffff", fg="#fede3f")
        self.lab2.pack(pady=15)
        
        self.title = Label(self.lab2, text='Patient\'s Detail Form', font=('Helvetica', 22, 'italic'), bg='#fff', fg="#fece2f").grid(row=0, column=0,pady=25)
                             
        self.namelab = Label(self.lab2, text='Full Name : ', font=('Coda Regular', 12), justify='left', width  = 28, bg='#fff', fg="#000").grid(row=1, column=0)
        self.nameent = Entry(self.lab2, textvariable = self.pname, font=('Coda Regular', 18),bd=3, bg='#fff', fg="#000").grid(row=2, column=0,pady=8)
                             
        self.namelab = Label(self.lab2, text='Phone Number : ', font=('Coda Regular', 12), width = 28, bg='#fff', fg="#000").grid(row=3, column=0)
        self.nameent = Entry(self.lab2, textvariable = self.pnumber, font=('Coda Regular', 18), bd=3, bg='#fff', fg="#000").grid(row=4, column=0,pady=8)
                                                     
        self.namelab = Label(self.lab2, text='Email ID : ', font=('Coda Regular', 12), width  = 28, bg='#fff', fg="#000").grid(row=5, column=0)
        self.nameent = Entry(self.lab2, textvariable = self.pemail, font=('Coda Regular', 18), bd=3, bg='#fff', fg="#000").grid(row=6, column=0,pady=8)
                                    
        self.namelab = Label(self.lab2, text='Date of Birth : ', font=('Coda Regular', 12), width  = 28, bg='#fff', fg="#000").grid(row=7, column=0)
        self.nameent = Entry(self.lab2, textvariable = self.pdob, font=('Coda Regular', 18), bd=3, bg='#fff', fg="#000").grid(row=8, column=0,pady=8)
                                   
        self.namelab = Label(self.lab2, text='Blood Group : ', font=('Coda Regular', 12), width  = 28, bg='#fff', fg="#000").grid(row=9, column=0)
        self.nameent = Entry(self.lab2, textvariable = self.pbloodgr, font=('Coda Regular', 18), bd=3, bg='#fff', fg="#000").grid(row=10, column=0,pady=8)
                                    
        self.namelab = Label(self.lab2, text='Gender : ', font=('Coda Regular', 12), width  = 28, bg='#fff', fg="#000").grid(row=11, column=0)
        self.nameent = Entry(self.lab2, textvariable = self.pgender, font=('Coda Regular', 18), bd=3, bg='#fff', fg="#000").grid(row=12, column=0,pady=8)
        
        self.genat = Button(self.lab2, image=self.genqr, bd=0, bg='white', fg='white', command = lambda: self.qrdis())
        self.genat.grid(row=13, column=0,pady=18)
                             



    def qrdis(self):
        s=self.pnumber.get()       
        big_code = pyqrcode.create(s, error='L', version=1, mode='binary')
        big_code.png(str(s), scale=6, module_color=[58, 0, 58, 128], background=[58, 210, 216])
        big_code.show()
        
                                 
        

        
        
if __name__ == '__main__':
    #Create Object
    #and setup window
    root1 = Tk()
    root1.title('Vigour')
    root1.geometry('346x690')
    #root1.state("zoomed")
    main(root1)
    root1.mainloop()        