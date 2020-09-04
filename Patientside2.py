# import library 
import math, random
import vlc
from tkinter import *
import datetime
import time
from tkinter import messagebox as m
from firebase import firebase
'from passengerDetailsGUI import *'
'from reservationGUI import *'
import sqlite3

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days = 1)
past = today - datetime.timedelta(days = 2)

def generateOTP() : 
    digits = "0123456789"
    OTP = "" 
    for i in range(4) : 
        OTP += digits[math.floor(random.random() * 10)] 
  
    return OTP
OTP=generateOTP

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
        self.depart = []
        self.dat = []
        self.tim = []

        res1 = FBConn.get('/IVR/', None)
        item = str(past)
        for key in res1.keys():
            if item in res1[key]:
                c=key 
                FBConn.delete('/IVR/',c)
         
            
        #Create Widgets
        self.image13 = PhotoImage(file='logo1.png', height=140, width=140)
        self.image14 = PhotoImage(file='user.png', height=150, width=150)
        self.widgets1()


    #Draw Widgets
    def widgets1(self):
        self.mainframe = Frame(self.master, bg='#ffffff', width=346, height=690)
        self.mainframe.pack(fill=BOTH)
        # 1st frame
        self.lab = Label(self.mainframe,text=' ', font=('Helvetica', 30, 'bold italic'), bg="#ffffff", fg="#ffffff")
        self.lab.pack(fill=BOTH)
        self.l1 = Label(self.lab, bg="#ffffff")
        self.l1.pack(fill=BOTH)
        self.f1 = Frame(self.l1, bg="#ffffff")
        self.f1.pack(fill=BOTH, side=TOP)

        self.head1 = Label(self.f1, image=self.image13, bg="#ffffff", fg="#ffffff")
        self.head1.grid(row=0, column=0, padx=103, pady=200)
        self.head2 = Label(self.f1, text='Vigour', font=('Helvetica', 25, 'bold italic'), bg="#ffffff", fg="#fece2f")
        self.head2.grid(row=1, column=0, padx=90, ipady=10)
        self.head2 = Label(self.f1, text=' ', font=('Helvetica', 25, 'bold italic'), bg="#ffffff", fg="#fece2f")
        self.head2.grid(row=2, column=0, padx=100, ipady=10)
        self.l1.after(3000, lambda: self.lab.destroy())
        
        
        self.lab1 = Label(self.mainframe,text=' ', font=('Helvetica', 30, 'bold italic'), bg="#ffffff", fg="#ffffff")
        self.lab1.pack(fill=BOTH)
        self.l2 = Label(self.lab1, bg="#ffffff")
        self.l2.pack(fill=BOTH)
        self.f2 = Frame(self.l2, bg="#ffffff")
        self.f2.pack(fill=BOTH, side=TOP)

        self.head3 = Label(self.f2, image=self.image14, bg="#ffffff", fg="#ffffff")
        self.head3.grid(row=0, column=0, padx=98, pady=100)
        self.head4 = Label(self.f2, text='Call... Vigour', font=('Helvetica', 15, 'italic'), bg="#ffffff", fg="#fece2f")
        self.head4.grid(row=1, column=0, padx=75, ipady=0)
        self.head5 = Label(self.f2, text='1081071081', font=('Helvetica', 15, 'bold'), bg="#ffffff", fg="#fece2f")
        self.head5.grid(row=2, column=0, padx=100, ipady=2)
        self.head6 = Label(self.f2, text= ' ', font=('Helvetica', 35, 'bold'), bg="#ffffff", fg="#fece2f")
        self.head6.grid(row=3, column=0, padx=100, ipady=100)
        self.banswer = Button(self.f2,bg='#ffffff',borderwidth=0, command = self.fframe)
        self.banswer.place(x=140, y=510)
        self.file1 = PhotoImage(file="answer.png",height=420, width=420)
        self.banswer.config(image=self.file1, compound=CENTER)
        self.file2 = self.file1.subsample(7, 7)
        self.banswer.config(image=self.file2)
        
    def fframe(self):
        self.lab1.destroy()
        self.lab2 = Label(self.mainframe,text=' ', font=('Helvetica', 30, 'bold italic'), bg="#ffffff", fg="#ffffff")
        self.lab2.pack(fill=BOTH)
        self.l3 = Label(self.lab2, bg="#ffffff")
        self.l3.pack(fill=BOTH)
        self.f3 = Frame(self.l3, bg="#ffffff")
        self.f3.pack(fill=BOTH, side=TOP)
        self.head3 = Label(self.f3, image=self.image14, bg="#ffffff", fg="#ffffff")
        self.head3.grid(row=0, column=0, padx=98, pady=100)
        self.head4 = Label(self.f3, text='Calling... Vigour', font=('Helvetica', 15, 'italic'), bg="#ffffff", fg="#fece2f")
        self.head4.grid(row=1, column=0, padx=75, ipady=0)
        self.head5 = Label(self.f3, text='1081071081', font=('Helvetica', 15, 'bold'), bg="#ffffff", fg="#fece2f")
        self.head5.grid(row=2, column=0, padx=100, ipady=2)
        self.head6 = Label(self.f3, text= ' ', font=('Helvetica', 35, 'bold'), bg="#ffffff", fg="#fece2f")
        self.head6.grid(row=3, column=0, padx=100, ipady=100)
        self.l3.after(500, lambda: self.lab2.destroy())

        self.sound_file = vlc.MediaPlayer("department.mp3")
        self.sound_file.play()

        self.lab5 = Label(self.mainframe, text=' ', font=('Helvetica', 30, 'bold italic'), bg="#ffffff", fg="#ffffff", width=346, height=690)
        self.lab5.pack(fill=BOTH)

        self.frame = Frame(self.lab5, width=346, height=690, bg='#ffffff')
        self.frame.pack()
    
        self.txt = Text(self.frame, width=40, height=12, wrap=WORD, bg='#eceff1')
        self.txt.place(x=11,y=20)
        
        self.b1 = Button(self.frame,text='1', padx=24, pady=24, bg='#fece2f', command = self.dental)
        self.b1.place(x=22, y=240)
        self.b2 = Button(self.frame,text='2', padx=24, pady=24, bg='#fece2f', command = self.ent)
        self.b2.place(x=140, y=240)
        self.b3 = Button(self.frame,text='3', padx=24, pady=24, bg='#fece2f', command = self.neuro)
        self.b3.place(x=259, y=240)
        self.b4 = Button(self.frame,text='4', padx=24, pady=24, bg='#fece2f')
        self.b4.place(x=22, y=330)
        self.b5 = Button(self.frame,text='5', padx=24, pady=24, bg='#fece2f')
        self.b5.place(x=140, y=330)
        self.b6 = Button(self.frame,text='6', padx=24, pady=24, bg='#fece2f')
        self.b6.place(x=259, y=330)
        self.b7 = Button(self.frame,text='7', padx=24, pady=24, bg='#fece2f')
        self.b7.place(x=22, y=420)
        self.b8 = Button(self.frame,text='8', padx=24, pady=24, bg='#fece2f')
        self.b8.place(x=140, y=420)
        self.b9 = Button(self.frame,text='9', padx=24, pady=24, bg='#fece2f')
        self.b9.place(x=259, y=420)
        self.b10 = Button(self.frame,text='*', padx=24, pady=24, bg='#fece2f')
        self.b10.place(x=22, y=510)
        self.b11 = Button(self.frame,text='0', padx=24, pady=24, bg='#fece2f')
        self.b11.place(x=140, y=510)
        self.b12 = Button(self.frame,text='#', padx=24, pady=24, bg='#fece2f')
        self.b12.place(x=259, y=510)
        
        self.breject = Button(self.frame,bg='#ffffff',borderwidth=0, command = self.stop_sound)
        self.breject.place(x=140, y=610)
        self.file3 = PhotoImage(file="reject.png",height=420, width=420)
        self.breject.config(image=self.file3, compound=CENTER)
        self.file4 = self.file3.subsample(7, 7)
        self.breject.config(image=self.file4)
    
    def stop_sound(self):
        self.sound_file.stop()
        root1.destroy()
        
        
    def dental(self):
        self.depart.append('Dental')
        self.department()
        
    def ent(self):
        self.depart.append('ENT')
        self.department()
         
    def neuro(self):
        self.depart.append('Neurology')
        self.department()        
        
        
        

    def department(self):
        self.lab5.destroy()
        self.lab6 = Label(self.mainframe, text=' ', font=('Helvetica', 30, 'bold italic'), bg="#ffffff", fg="#ffffff", width=346, height=690)
        self.lab6.pack(fill=BOTH)

        self.frame = Frame(self.lab6, width=346, height=690, bg='#ffffff')
        self.frame.pack()
    
        self.sound_file.stop()
        self.sound_file = vlc.MediaPlayer("date.mp3")
        self.sound_file.play()

        self.txt = Text(self.frame, width=40, height=12, wrap=WORD, bg='#eceff1')
        self.txt.place(x=11,y=20)
        
        self.b1 = Button(self.frame,text='1', padx=24, pady=24, bg='#fece2f', command = self.date1)
        self.b1.place(x=22, y=240)
        self.b2 = Button(self.frame,text='2', padx=24, pady=24, bg='#fece2f', command = self.date2)
        self.b2.place(x=140, y=240)
        self.b3 = Button(self.frame,text='3', padx=24, pady=24, bg='#fece2f')
        self.b3.place(x=259, y=240)
        self.b4 = Button(self.frame,text='4', padx=24, pady=24, bg='#fece2f')
        self.b4.place(x=22, y=330)
        self.b5 = Button(self.frame,text='5', padx=24, pady=24, bg='#fece2f')
        self.b5.place(x=140, y=330)
        self.b6 = Button(self.frame,text='6', padx=24, pady=24, bg='#fece2f')
        self.b6.place(x=259, y=330)
        self.b7 = Button(self.frame,text='7', padx=24, pady=24, bg='#fece2f')
        self.b7.place(x=22, y=420)
        self.b8 = Button(self.frame,text='8', padx=24, pady=24, bg='#fece2f')
        self.b8.place(x=140, y=420)
        self.b9 = Button(self.frame,text='9', padx=24, pady=24, bg='#fece2f')
        self.b9.place(x=259, y=420)
        self.b10 = Button(self.frame,text='*', padx=24, pady=24, bg='#fece2f')
        self.b10.place(x=22, y=510)
        self.b11 = Button(self.frame,text='0', padx=24, pady=24, bg='#fece2f')
        self.b11.place(x=140, y=510)
        self.b12 = Button(self.frame,text='#', padx=24, pady=24, bg='#fece2f')
        self.b12.place(x=259, y=510)

        self.breject = Button(self.frame,bg='#ffffff',borderwidth=0, command = self.stop_sound)
        self.breject.place(x=140, y=610)
        self.file3 = PhotoImage(file="reject.png",height=420, width=420)
        self.breject.config(image=self.file3, compound=CENTER)
        self.file4 = self.file3.subsample(7, 7)
        self.breject.config(image=self.file4)
        
    def date1(self):
        self.dat.append(today)
        self.date()
        
    def date2(self):
        self.dat.append(tomorrow)
        self.date()

        
        

    def date(self):
        self.lab6.destroy()
        self.lab7 = Label(self.mainframe, text=' ', font=('Helvetica', 30, 'bold italic'), bg="#ffffff", fg="#ffffff", width=346, height=690)
        self.lab7.pack(fill=BOTH)

        self.frame = Frame(self.lab7, width=346, height=690, bg='#ffffff')
        self.frame.pack()
        
        self.sound_file.stop()
        self.sound_file = vlc.MediaPlayer("time.mp3")
        self.sound_file.play()
        
        self.txt = Text(self.frame, width=40, height=12, wrap=WORD, bg='#eceff1')
        self.txt.place(x=11,y=20)
        
        self.b1 = Button(self.frame,text='1', padx=24, pady=24, bg='#fece2f', command = self.time1)
        self.b1.place(x=22, y=240)
        self.b2 = Button(self.frame,text='2', padx=24, pady=24, bg='#fece2f', command = self.time2)
        self.b2.place(x=140, y=240)
        self.b3 = Button(self.frame,text='3', padx=24, pady=24, bg='#fece2f', command = self.time3)
        self.b3.place(x=259, y=240)
        self.b4 = Button(self.frame,text='4', padx=24, pady=24, bg='#fece2f')
        self.b4.place(x=22, y=330)
        self.b5 = Button(self.frame,text='5', padx=24, pady=24, bg='#fece2f')
        self.b5.place(x=140, y=330)
        self.b6 = Button(self.frame,text='6', padx=24, pady=24, bg='#fece2f')
        self.b6.place(x=259, y=330)
        self.b7 = Button(self.frame,text='7', padx=24, pady=24, bg='#fece2f')
        self.b7.place(x=22, y=420)
        self.b8 = Button(self.frame,text='8', padx=24, pady=24, bg='#fece2f')
        self.b8.place(x=140, y=420)
        self.b9 = Button(self.frame,text='9', padx=24, pady=24, bg='#fece2f')
        self.b9.place(x=259, y=420)
        self.b10 = Button(self.frame,text='*', padx=24, pady=24, bg='#fece2f')
        self.b10.place(x=22, y=510)
        self.b11 = Button(self.frame,text='0', padx=24, pady=24, bg='#fece2f')
        self.b11.place(x=140, y=510)
        self.b12 = Button(self.frame,text='#', padx=24, pady=24, bg='#fece2f')
        self.b12.place(x=259, y=510)

        self.breject = Button(self.frame,bg='#ffffff',borderwidth=0, command = self.stop_sound)
        self.breject.place(x=140, y=610)
        self.file3 = PhotoImage(file="reject.png",height=420, width=420)
        self.breject.config(image=self.file3, compound=CENTER)
        self.file4 = self.file3.subsample(7, 7)
        self.breject.config(image=self.file4)
        
    def time1(self):
        self.tim.append('7:00 PM')
        res1 = FBConn.get('/IVR/', None)
        rev = list(res1.values())
        cl=[]
        for row in rev:
            cl.append(row[0:3])
        ck=str(self.dat[0])   
        navl=[[self.depart[0],ck,self.tim[0]]]
        dek = self.checkapp(cl,navl)
        if dek == True:
            self.sorry()
            
        else:
            self.confir()

    def time2(self):
        self.tim.append('7:00 PM')
        res1 = FBConn.get('/IVR/', None)
        rev = list(res1.values())
        cl=[]
        for row in rev:
            cl.append(row[0:3])
        ck=str(self.dat[0])  
        navl=[[self.depart[0],self.dat[0],self.tim[0],OTP]]
        dek = self.checkapp(cl,navl)
        if dek == True:
            self.sorry()
            
        else:
            self.confir()

    def time3(self):
        self.tim.append('7:00 PM')
        res1 = FBConn.get('/IVR/', None)
        rev = list(res1.values())
        cl=[]
        for row in rev:
            cl.append(row[0:3])
        ck=str(self.dat[0])  
        navl=[[self.depart[0],self.dat[0],self.tim[0],OTP]]
        dek = self.checkapp(cl,navl)
        if dek == True:
            self.sorry()    
        else:
            self.confir()            
        
    def time5(self):
        self.tim.append('7:30 PM')
        self.confir()
         
    def time6(self):
        self.tim.append('8:30 PM')
        self.confir()        
        
    
    def checkapp(self,l,s):
          sub_set = False
          if s == []:
              sub_set = True
          elif s == l:
              sub_set = True
          elif len(s) > len(l):
              sub_set = False
          else:
              for i in range(len(l)):
                  if l[i] == s[0]:
                      n = 1
                      while (n < len(s)) and (l[i+n] == s[n]):
                          n += 1
                                  
                      if n == len(s):
                          sub_set = True
          return sub_set        
        
    
    
    def sorry(self):
        self.lab7.destroy()
        self.lb8 = Label(self.mainframe, text=' ', font=('Helvetica', 30, 'bold italic'), bg="#ffffff", fg="#ffffff", width=346, height=690)
        self.lb8.pack(fill=BOTH)

        self.frame = Frame(self.lb8, width=346, height=690, bg='#ffffff')
        self.frame.pack()
        
        self.sound_file.stop()
        self.sound_file = vlc.MediaPlayer("sorry.mp3")
        self.sound_file.play()
        
        
        self.txt = Text(self.frame, width=40, height=12, wrap=WORD, bg='#eceff1')
        self.txt.place(x=11,y=20)
        
        self.b1 = Button(self.frame,text='1', padx=24, pady=24, bg='#fece2f')
        self.b1.place(x=22, y=240)
        self.b2 = Button(self.frame,text='2', padx=24, pady=24, bg='#fece2f')
        self.b2.place(x=140, y=240)
        self.b3 = Button(self.frame,text='3', padx=24, pady=24, bg='#fece2f')
        self.b3.place(x=259, y=240)
        self.b4 = Button(self.frame,text='4', padx=24, pady=24, bg='#fece2f')
        self.b4.place(x=22, y=330)
        self.b5 = Button(self.frame,text='5', padx=24, pady=24, bg='#fece2f')
        self.b5.place(x=140, y=330)
        self.b6 = Button(self.frame,text='6', padx=24, pady=24, bg='#fece2f')
        self.b6.place(x=259, y=330)
        self.b7 = Button(self.frame,text='7', padx=24, pady=24, bg='#fece2f')
        self.b7.place(x=22, y=420)
        self.b8 = Button(self.frame,text='8', padx=24, pady=24, bg='#fece2f')
        self.b8.place(x=140, y=420)
        self.b9 = Button(self.frame,text='9', padx=24, pady=24, bg='#fece2f')
        self.b9.place(x=259, y=420)
        self.b10 = Button(self.frame,text='*', padx=24, pady=24, bg='#fece2f')
        self.b10.place(x=22, y=510)
        self.b11 = Button(self.frame,text='0', padx=24, pady=24, bg='#fece2f', command = self.reset1)
        self.b11.place(x=140, y=510)
        self.b12 = Button(self.frame,text='#', padx=24, pady=24, bg='#fece2f')
        self.b12.place(x=259, y=510)

        self.breject = Button(self.frame,bg='#ffffff',borderwidth=0, command = self.stop_sound)
        self.breject.place(x=140, y=610)
        self.file3 = PhotoImage(file="reject.png",height=420, width=420)
        self.breject.config(image=self.file3, compound=CENTER)
        self.file4 = self.file3.subsample(7, 7)
        self.breject.config(image=self.file4)


    def reset1(self):
        self.lb8.destroy()
        self.depart = []
        self.dat = []
        self.tim = []
        self.fframe()
            


    def confir(self):
        self.lab7.destroy()
        self.lab8 = Label(self.mainframe, text=' ', font=('Helvetica', 30, 'bold italic'), bg="#ffffff", fg="#ffffff", width=346, height=690)
        self.lab8.pack(fill=BOTH)

        self.frame = Frame(self.lab8, width=346, height=690, bg='#ffffff')
        self.frame.pack()
        
        self.sound_file.stop()
        self.sound_file = vlc.MediaPlayer("confirm.mp3")
        self.sound_file.play()
        
        
        self.txt = Text(self.frame, width=40, height=12, wrap=WORD, bg='#eceff1')
        self.txt.place(x=11,y=20)
        
        self.b1 = Button(self.frame,text='1', padx=24, pady=24, bg='#fece2f', command = self.success)
        self.b1.place(x=22, y=240)
        self.b2 = Button(self.frame,text='2', padx=24, pady=24, bg='#fece2f')
        self.b2.place(x=140, y=240)
        self.b3 = Button(self.frame,text='3', padx=24, pady=24, bg='#fece2f')
        self.b3.place(x=259, y=240)
        self.b4 = Button(self.frame,text='4', padx=24, pady=24, bg='#fece2f')
        self.b4.place(x=22, y=330)
        self.b5 = Button(self.frame,text='5', padx=24, pady=24, bg='#fece2f')
        self.b5.place(x=140, y=330)
        self.b6 = Button(self.frame,text='6', padx=24, pady=24, bg='#fece2f')
        self.b6.place(x=259, y=330)
        self.b7 = Button(self.frame,text='7', padx=24, pady=24, bg='#fece2f')
        self.b7.place(x=22, y=420)
        self.b8 = Button(self.frame,text='8', padx=24, pady=24, bg='#fece2f')
        self.b8.place(x=140, y=420)
        self.b9 = Button(self.frame,text='9', padx=24, pady=24, bg='#fece2f')
        self.b9.place(x=259, y=420)
        self.b10 = Button(self.frame,text='*', padx=24, pady=24, bg='#fece2f')
        self.b10.place(x=22, y=510)
        self.b11 = Button(self.frame,text='0', padx=24, pady=24, bg='#fece2f', command = self.reset)
        self.b11.place(x=140, y=510)
        self.b12 = Button(self.frame,text='#', padx=24, pady=24, bg='#fece2f')
        self.b12.place(x=259, y=510)

        self.breject = Button(self.frame,bg='#ffffff',borderwidth=0, command = self.stop_sound)
        self.breject.place(x=140, y=610)
        self.file3 = PhotoImage(file="reject.png",height=420, width=420)
        self.breject.config(image=self.file3, compound=CENTER)
        self.file4 = self.file3.subsample(7, 7)
        self.breject.config(image=self.file4)


    def reset(self):
        self.lab8.destroy()
        self.depart = []
        self.dat = []
        self.tim = []
        self.fframe()
        
    def success(self):
        k =[self.depart[0],self.dat[0],self.tim[0],OTP]
        
        result = FBConn.post('/IVR/', k)
        m.showinfo("OTP",message='Please remember this OTP : '+ OTP)


    


             
if __name__ == '__main__':
    #Create Object
    #and setup window
    root1 = Tk()
    root1.title('Vigour')
    #root.geometry('1366x768')
    #root1.state("zoomed")
    main(root1)
    root1.mainloop()

