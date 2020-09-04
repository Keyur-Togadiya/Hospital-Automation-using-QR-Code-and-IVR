from gtts import gTTS
import time

text2 = "Welcome to Vigour. Please Select a relevant department. For booking an appointment. Press 1 for Dental. Press 2 for ENT.Press 3 for Neurology."
text5 = "For Booking Today's appointment Press 1 . For booking tomorrow's appointment press 2."
text6 = "Please select time as per your preference Press 1 for 7:00 PM. Press 2 for 7:30 PM. Press 3 for 8:00 PM"
text7 = "To Confirm booking of Appointment Press 1. To go back to the main menu Press 0."
text8 = "We are very sorry. Appointmet for this slot has already been booked. Try booking for another slot. Press 0 to go to main menu. Press reject to stop booking process.  "



speech2 = gTTS(text2)
speech5 = gTTS(text5)
speech6 = gTTS(text6)
speech7 = gTTS(text7)
speech8 = gTTS(text8)




speech2.save("department.mp3")
speech5.save("date.mp3")
speech6.save("time.mp3")
speech7.save("confirm.mp3")
speech8.save("sorry.mp3")

'''# import library 
import math, random
import sqlite3
import datetime


con = sqlite3.connect('abcd.db')
c = con.cursor()

# function to generate OTP 
def generateOTP() : 
  
    # Declare a digits variable   
    # which stores all digits  
    digits = "0123456789"
    OTP = "" 
  
   # length of password can be chaged 
   # by changing value in range 
    for i in range(4) : 
        OTP += digits[math.floor(random.random() * 10)] 
  
    return OTP


now = datetime.now()

dated = now.strftime("%H:%M")
print("Current Time =", dated)
  
# Driver code 
if __name__ == "__main__" : 
      
    print("OTP of 4 digits:", generateOTP())
    print("Current date:", dated)

    c.execute(CREATE TABLE IF NOT EXISTS dateotp(Date TIME, otp INT))
    c.execute('INSERT INTO dateotp(Date,otp) VALUES(?,?)',(dated, generateOTP()))
    c.execute('SELECT * FROM dateotp')
    print(c.fetchall())
    con.commit()'''
