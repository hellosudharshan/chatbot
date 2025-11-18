import pyttsx3;
import time;
import mysql.connector;
import speech_recognition as sr;
import os
import subprocess
import screen_brightness_control as sbc
import pprint
from playsound import playsound
from pprint import pprint
from gtts import gTTS
import pyttsx3;
from googletrans import Translator, constants
from pydub import AudioSegment
from pydub.silence import split_on_silence
import webbrowser
import datetime
import wikipedia
import requests
import pywintypes
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations
from bs4 import BeautifulSoup
import win32gui, win32con
import os
import math
import numpy as np
import pandas as pd 
import random
import pyautogui
import pywhatkit
import PyPDF2
import docx;
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer


#==================================================   voice function to convert text to speech

def voice(txt):
    engine = pyttsx3.init();
    # Set Rate / speed
    engine.setProperty('rate', 150)
    #voices = engine.getProperty('voices')
    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    #engine.setProperty('voice', voices[sv].id)
    
    # Set Volume
    engine.setProperty('volume', 5.0)
    engine.say(txt);
    engine.runAndWait() ;


numw = 1
numw2=1
def tvoice(output):
    global numw

    # num to rename every audio file
    # with different name to remove ambiguity
    numw += 1
    print("Kural : ", output)

    toSpeak = gTTS(text = output, lang ='ta', slow = False)
    # saving the audio file given by google text to speech
    file = str(num)+".mp3"
    toSpeak.save(file)
    
    # playsound package is used to play the same file.
    playsound(file, True)
    os.remove(file)

chatbot=ChatBot('inirah')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings","chatterbot.corpus.english.conversations" )

def printsv(text):
    from plyer import notification
    notification.notify(title = "Tris",message=text ,timeout=2)

#----------------------------------------------------------------------

con=mysql.connector.connect(host='localhost',user='root',passwd='',database='')
mycursor=con.cursor()

try:
    mycursor.execute("CREATE DATABASE assis")
    mycursor.execute("USE assis")
    #print("Database created")

except:
    mycursor.execute("USE assis")
    #print("Database Enhanced")

try:
    command="CREATE TABLE user(Id int(50) PRIMARY KEY,Name char(30))"
    mycursor.execute(command)
    #print("Table has been created")

except:
    #print("TABLE ENHANCED")
    'No problem'
os.system('cls')
while True:
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n> Start the System ?")
    asd=input()
    if asd=="lakshmi start":
        break

voice("Welcome to Integrated virtual automated machine system")
#Label(ws, text = 'Integrated Virtual Automated Machine System').pack(side = TOP, pady = 20)

time.sleep(1)
voice("Please enter your id to proceed")

num=int(input("Enter the your ID :"))


mycursor.execute("SELECT Id FROM user")
data=mycursor.fetchall()

ctr=0

for row in data:
    for a in row:
        row2=a
        if num==row2:
            #print("Already Present!!!")
            ctr=1
            break

if ctr==0:
    print("New User! \nCan We Create ???")
    printsv("New User! \nCan We Create ???")
    voice("New User! \nCan We Create ???")
    n2=input("Enter Your Name :")

    while True:
        sv=0
        num=int(input("Enter Your Id :"))
        mycursor.execute("SELECT Id FROM user")
        data=mycursor.fetchall()
        for row in data:
            for a in row:
                row2=a
                if num==row2:
                    print("Already Present!!!\nTry with another ID!!! ")
                    printsv("Already Present!!!\nTry with another ID!!! ")
                else:
                    sv=1
                if sv==1:
                    break
            if sv==1:
                break
        if sv==1:
            break
    mycursor.execute("INSERT INTO user VALUES({},'{}')".format(num,n2))
    #print("Added data")
    con.commit()


mycursor.execute("SELECT Name FROM user WHERE Id={}".format(num))
nam=mycursor.fetchall()
playsound("aandava.mp3")
for n1 in nam:
    for n2 in n1:
        print("Welcome back ",n2)
        printsv("Welcome back "+str(n2))
        name="welcome back "+n2
        voice(name)

#---------------------------------------  finding name male or female and setting z as sir or mam
vb=['a','e','i','A','E','I']
for c in vb:
    if (n2[len(n2)-1])== c:
        z='Mam'
        break
    else:
        z="Sir"

        
#                                       n2 is the name of the user and num is the id


#---------------------------------------------------------------------- Telling time and greeting

time.sleep(1)
a=time.asctime(time.localtime(time.time()))
b,c,d,e,f,g,h,i=a[:3],a[4:7],a[8:10],a[11:19],a[20:],int(a[11:13]),int(a[14:16]),int(a[17:19])
if g>=0 and g<4:
    print("Itz Mid Night "+z+"!!!\nStill",6-g,"Hours to dawn!!!")
    printsv("Itz Mid Night "+z+"!!!\nStill"+str(6-g)+"Hours to dawn!!!")
    greet="Itz Mid Night"+z
if g>=4 and g<7:
    print("Its Early Moring "+z+"!!!")
    printsv("Its Early Moring "+z+"!!!")
    greet="Its Early Moring"+z
if g>=7 and g<12:
    print("Good Morning "+z+"!!!")
    printsv("Good Morning "+z+"!!!")
    greet="Good Morning "+z
if g>=12 and g<16:
    print("Good Afternoon "+z+"!!")
    printsv("Good Afternoon "+z+"!!")
    greet="Good Afternoon "+z
if g>=16 and g<20:
    print("Good Evening "+z+"!!!")
    printsv("Good Evening "+z+"!!!")
    greet="Good Evening "+z
if g>=20:
    print("Seems we are gonna have a wonderful night today "+z)
    printsv("Seems we are gonna have a wonderful night today "+z)
    greet="seems we are gonna have a wonderful night today "+z

voice(greet)


k=g
if g<1:
    k=12
if g>12:
    k=g-12
    
if g>=12:
    j="PM"
else:
    j="AM"
time.sleep(1)
print("\nDay   :",b)
print("Month :",c)
print('Date  :',d)
print('Year  :',f)
print('Time  :',e,"   OR   ",k,":",h,":",i,j)
printsv("\nDay   :"+str(b)+"\nMonth :"+str(c)+'\nDate  :'+str(d)+'\nYear  :'+str(f)+'\nTime  :'+str(e)+"   OR   "+str(k)+":"+str(h)+":"+str(i)+j)

greet20="time is %d"%k
greet2=greet20+" "+str(h)+j                      # telling time

voice(greet2)

greet3=b+'day'+str(d)+"th"+" "+c+str(f)               # telling date and month

voice(greet3)

#==========================================================================================



# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def takeCommand():
    r = sr.Recognizer()
    # from the speech_Recognition module
    # we will use the Microphone module
    # for listening the command
    with sr.Microphone() as source:
        voice("at your service"+z)
        print('Listening')
    # seconds of non-speaking audio before
    # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)
    # Now we will be using the try and catch
        # method so that if sound is recognized
    # it is good else we will have exception handling
        try:
            print("Recognizing")
        # for Listening the command in indian
        # english we can also use 'hi-In'
        # for hindi recognizing
            Query = r.recognize_google(audio, language='en-in')
            print("Command : ", Query)
        except Exception as e:
            print(e)
            print("Say that again "+z)
            return "None"
        
        return Query

def Hello():
    # This function is for when the assistant
    # is called it will say hello and then
    # take query
    voice("Hello"+z+"! I'm Tris your virtual assistant. How can i help you?")

def wordre(filename):
    doc=docx.Document(filename)
    fullText=[]
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

def pdfre(filename):
    pdfFileObj = open(filename, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageObj = pdfReader.getPage(0)
    a=pageObj.extractText()
    pdfFileObj.close()
    return a

def tellDate():
    a=time.asctime(time.localtime(time.time()))
    b,c,d,e,f,g,h,i=a[:3],a[4:7],a[8:10],a[11:19],a[20:],int(a[11:13]),int(a[14:16]),int(a[17:19])
    greet3=b+'day'+str(d)+"th"+" "+c+str(f)               # telling date and month
    voice(greet3)
    
def tellTime(): 
    a=time.asctime(time.localtime(time.time()))
    b,c,d,e,f,g,h,i=a[:3],a[4:7],a[8:10],a[11:19],a[20:],int(a[11:13]),int(a[14:16]),int(a[17:19])
    k=g
    if g<1:
        k=12
    if g>12:
        k=g-12
    if g>=12:
        j="PM"
    else:
        j="AM"
    greet20="time is %d"%k
    greet2=greet20+" "+str(h)+j                      # telling time
    voice(greet2)

# Importing required modules
import os
import pyttsx3
import speech_recognition as sr



# Creating class
class Gfg:
    
    # Method to take choice commands as input
    def takeCommand(self):
        
        # Using Recognizer and Microphone Method for input voice commands
        r = sr.Recognizer()
        with sr.Microphone() as source:
                    print('Listening')
                    r.pause_threshold = 0.7
                    audio = r.listen(source)
                    try:
                        print("Recognizing")
                        Query = r.recognize_google(audio, language='en-in')
                        print("the query is printed='", Query, "'")
                    except Exception as e:
                        print(e)
                        print("Say that again sir")
                        return "None"
        return Query

    
    # Method for voice output
    def Speak(self, audio):

        # Constructor call for pyttsx3.init()
        engine = pyttsx3.init('sapi5')

        # Setting voice type and id
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()

    
    # Method to self shut down system
    def quitSelf(self):
        self.Speak("do u want to switch off the computer sir")

        # Input voice command
        take = self.takeCommand()
        choice = take
        if choice == 'yes':

            # Shutting down
            print("Shutting down the computer")
            self.Speak("Shutting the computer")
            os.system("shutdown /s /t 30")
        if choice =="no":
 
            # Idle
            print("Thank u sir")
            self.Speak("Thank u sir")

class Gfg2:
    
    # Method to take choice commands as input
    def takeCommand(self):
        
        # Using Recognizer and Microphone Method for input voice commands
        r = sr.Recognizer()
        with sr.Microphone() as source:
                        voice("At your service "+z)
                        print('Listening')
                        r.pause_threshold = 0.7
                        audio = r.listen(source)
                        try:
                            print("Recognizing")
                            Query = r.recognize_google(audio, language='en-in')
                            print("the query is printed='", Query, "'")
                        except Exception as e:
                            print(e)
                            print("Say that again sir")
                            return "None"
                        return Query
                
    def Speak(self, audio):

        # Constructor call for pyttsx3.init()
        engine = pyttsx3.init('sapi5')

        # Setting voice type and id
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(audio)
        engine.runAndWait()

    
    # Method to self shut down system
    def quitSelf(self):
        self.Speak("Do you want to restart the Computer?")

        # Input voice command
        take = self.takeCommand()
        choice = take
        if choice == 'yes':

            # Shutting down
            print("Restarting the System...")
            self.Speak("Restarting the system")
            os.system("shutdown /r /t 30")
        if choice == 'no':

            # Idle
            print("Thank you sir")
            self.Speak("Thank u sir")

def sharini():
    translator = Translator()
    def trans(text,sr='en',des='en'):
        translation = translator.translate(text, src=sr ,dest=des)
        print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
        output2 = str(translation.text)
        global numw2
        numw2 += 1
        toSpeak = gTTS(text = output2, lang =des, slow = False)
        file = str(numw2)+".mp3"
        toSpeak.save(file)
        playsound(file, True)
        os.remove(file)

    print("Total supported languages:", len(constants.LANGUAGES))
    print("Languages:")
    pprint(constants.LANGUAGES)
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say the text...")
        audio_data = r.record(source, duration=10)
        print("RECOGNIZING...")
        text = r.recognize_google(audio_data)
        print(text)
    detection = translator.detect(text)
    print("Language code:", detection.lang)
    print("Confidence:", detection.confidence)
    print("Language:", constants.LANGUAGES[detection.lang])
    b=input("enter the code of the language of the text:")
    text = r.recognize_google(audio_data, language=b)
    c=input("enter the code of the language to be converted:")
    trans(text,b,c)
    
def decv():
    try:
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        import math
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb - 10.0, None)
        volume.GetMasterVolumeLevel()

    except:
        print("Minimum Volume Attained "+z)
        voice("Minimum volume attained "+z)

def incv():
    try:
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        import math
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb + 10.0, None)
        volume.GetMasterVolumeLevel()

    except:
        print("Maximum Volume Attained "+z)
        voice("Maximum volume attained "+z)

def whether():
    print("Say the City Name...")
    city=takeCommand()
        
    url = "https://www.google.com/search?q="+"weather"+city
    html = requests.get(url).content
    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    
    # formatting data
    data = str.split('\n')
    time = data[0]
    sky = data[1]
    
    # getting all div tag
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text
    
    # getting other required data
    pos = strd.find('Wind')
    other_data = strd[pos:]
    
    # printing all data
    print("Temperature is", temp)
    print("Time: ", time)
    print("Sky Description: ", sky)
    print(other_data)
    voice("Temperature is"+temp+" \n Sky Description: "+sky)

def Take_query():
    # calling the Hello function for
    # making it more interactive
    Hello()
    # This loop is infinite as it will take
    # our queries continuously until and unless
    # we do not say bye to exit or terminate
    # the program
    while(True):    
        # taking the query and making it into
    # lower case so that most of the times
    # query matches and we get the perfect
    # output
        query = takeCommand().lower()
        if "open google" in query:
            voice("Opening Google ")
            webbrowser.open("www.google.com")
            continue

        elif "climate" in query:
            whether()
            
            
        elif "today date" in query:
            tellDate()
            continue
        
        elif "tell me the time" in query:
            tellTime()
            continue
        
    # this will exit and terminate the program
        elif "bye" in query:
            voice("Bye. Have a great day"+z)
            playsound("katham.mp3")
            exit()
        
        elif "search wikipedia" in query:
        # if any one wants to have a information
        # from wikipedia
            voice("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
        # it will give the summary of 4 lines from
        # wikipedia we can increase and decrease it also.
            result = wikipedia.summary(query, sentences=4)
            voice("According to wikipedia")
            voice(result)

        elif "legend" in query:
            playsound("sur.mp3")

        elif "translate" in query:
            sharini()

        elif "close" in query and"tata" in query:
            voice("Bye. Have a great day"+z)
            print("Shut down initiating...")
            playsound("katham.mp3")
            Maam = Gfg()
            Maam.quitSelf()

        elif "youtube" in query:
            print("What to search on ???")
            voice("What to search on "+z)
            yb=takeCommand().lower()
            

        elif "decrease brightness" in query:
            for bri in sbc.get_brightness():
                if bri<10:
                    sbc.set_brightness(0)
                else:
                    sbc.set_brightness(bri-10)

        elif "increase brightness" in query:
            for bri in sbc.get_brightness():
                if bri>90:
                    sbc.set_brightness(100)
                else:
                    sbc.set_brightness(bri+10)

        elif "close tab" in query:
            voice("say the app name...")
            print("Say the App Name...")
            cvbf=takeCommand().lower()
            subprocess.call(["taskkill","/F","/IM",cvbf+".exe"])

        elif "check running" in query:
            voice("say the app name...")
            print("Say the App Name...")
            cvbd=takeCommand().lower()
            import wmi
            f = wmi.WMI()
            flag = 0
            for process in f.Win32_Process():
                if cvbd+".exe" == process.Name:
                    print("Application is Running")
                    flag = 1
                    break
            if flag == 0:
                print("Application is not Running")

        
                
        elif "restart system" in query:
            voice("Bye. Have a great day"+z)
            print("Restart initiating...")
            playsound("katham.mp3")
            Maam = Gfg2()
            Maam.quitSelf()

        elif "tools" in query :
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')

            # changing index changes voices but only
            # 0 and 1 are working here
            engine.setProperty('voice', voices[1].id)
            engine.runAndWait()
            print("")
            print("")

            # introduction
            print(" =============================================== Hello World!! ================================================")
            engine.say('Hello World!!')
            
            print("")
            
            print("\n\t 1.MICROSOFT WORD \t 2.MICROSOFT POWERPOINT \n\t 3.MICROSOFT EXCEL \t 4.CALCULATOR \n\t 5.ANDROID STUDIO\t 6.VS CODE \n\t 7.WAMP SERVER \t \t 8.MICROSOFT EDGE \n\t 9.NOTEPAD     \t 10.ORACLE VBOX \n\n\t\t  0. FOR EXIT TOOLS")
            
            print("\n    (YOU CAN USE NUMBER OR YOU CAN DO CHAT LIKE 'OPEN NOTEBOOK' etc....)")
            
            print("\n ============================================ Welcome To My Tools ============================================")
            pyttsx3.speak("Welcome to my tools")
            print("")
            print("")

            pyttsx3.speak("chat with me with your requirements")
            
            while True:
                # take input
                print(" CHAT WITH ME WITH YOUR REQUIREMENTS : ", end='')
                p = input()
                p = p.upper()
                print(p)
                
                if ("DONT" in p) or ("DON'T" in p) or ("NOT" in p):
                    pyttsx3.speak("Type Again")
                    print(".")
                    print(".")
                    continue
                    
                    # assignments for different applications in the menu
                elif ("CALCULATOR" in p) or ("KANAKU" in p) or ("4" in p):
                    pyttsx3.speak("Opening")
                    pyttsx3.speak("CALCULATOR")
                    print(".")
                    print(".")
                    os.popen("CALC")
                    
                elif ("IE" in p) or ("MSEDGE" in p) or ("EDGE" in p) or ("8" in p):
                    pyttsx3.speak("Opening")
                    pyttsx3.speak("MICROSOFT EDGE")
                    print(".")
                    print(".")
                    os.popen("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
                    
                elif ("NOTE" in p) or ("NOTES" in p) or ("NOTEPAD" in p) or ("EDITOR" in p) or ("9" in p):
                    pyttsx3.speak("Opening")
                    pyttsx3.speak("NOTEPAD")
                    print(".")
                    print(".")
                    os.popen("Notepad")

                elif ("APPLICATION BUIDER" in p) or ("ANDROID STUDIO" in p) or ("APP BUILD" in p) or ("5" in p):
                    pyttsx3.speak("Opening")
                    pyttsx3.speak("ANDROID STUDIO")
                    print(".")
                    print(".")
                    os.popen("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Android Studio\Android Studio.lnk")
                
                elif ("VS CODE" in p) or ("HTML EDITOR" in p) or ("6" in p):
                    pyttsx3.speak("Opening")
                    pyttsx3.speak("VS CODE")
                    print(".")
                    print(".")
                    os.popen(r"C:\Users\91962\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")
                
                elif ("WAMP" in p) or ("LOCAL SERVER" in p) or ("LOCALSERVER" in p) or ("7" in p):
                    pyttsx3.speak("Opening")
                    pyttsx3.speak("GMEET")
                    print(".")
                    print(".")
                    os.popen(r"C:\Users\Public\Desktop\Wampserver32.lnk")
                    
                elif ("ORACLE VBOX" in p) or ("VB" in p) or ("10" in p):
                    pyttsx3.speak("Opening")
                    pyttsx3.speak("ORACLE VIRTUALBOX")
                    print(".")
                    print(".")
                    os.popen("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Oracle VM VirtualBox\Oracle VM VirtualBox.lnk")
                
                elif ("EXCEL" in p) or ("MSEXCEL" in p) or ("SHEET" in p) or ("WINEXCEL" in p) or ("3" in p):
                    pyttsx3.speak("Opening")
                    pyttsx3.speak("MICROSOFT EXCEL")
                    print(".")
                    print(".")
                    os.popen("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk")
                
                elif ("SLIDE" in p) or ("MSPOWERPOINT" in p) or ("PPT" in p) or ("POWERPNT" in p) or ("2" in p):
                    pyttsx3.speak("Opening")
                    pyttsx3.speak("MICROSOFT POWERPOINT")
                    print(".")
                    print(".")
                    os.popen("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk")
                
                elif ("WORD" in p) or ("MSWORD" in p) or ("1" in p):
                    pyttsx3.speak("Opening")
                    pyttsx3.speak("MICROSOFT WORD")
                    print(".")
                    print(".")
                    os.popen("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")
                
                # close the program
                elif ("EXIT" in p) or ("QUIT" in p) or ("CLOSE" in p) or ("0" in p):
                    pyttsx3.speak("Exiting Tools")
                    break
                
                # for invalid input
                else:
                    pyttsx3.speak(p)
                    print("Is Invalid,Please Try Again")
                    pyttsx3.speak("is Invalid,Please try again")
                    print(".")
                    print(".")
                
        elif "file manager" in query:
            # take Input from the user
            query = input("Which drive you have to open ? C , D or E: \n")
            # Check the condition for
            # opening the C drive
            if "C" in query or "c" in query:
                os.startfile("C:")
                # Check the condition for
                # opening the D drive
            elif "D" in query or "d" in query:
                os.startfile("D:")
                # Check the condition for
                # opening the D drive
            elif "E" in query or "e" in query:
                os.startfile("E:")
            elif "O" in query or "o" in query:
                myf=input("Enter the name of file with its path:")
                os.startfile(myf)
            else:
                print("Wrong Input")
        
              
        elif "message" in query:
            voice("Please Enter The Message To Be Sent Sir")
            message=input("Please Enter The Message To Be Sent :")
            voice("Please Enter the number you wish to sent")
            cont=input("Please Enter the number you wish to sent :")
            hr=int(input("Enter Hour :"))
            minu=int(input("Enter Minute :"))
            # syntax: phone number with country code, message, hour and minutes
            pywhatkit.sendwhatmsg('+91'+cont, message , hr, minu)

        elif "what can you do" in query:
            print("Commands : \nOpen Google\nClimate\nTodays Date\nTell Me The Time\nSearch Wikipedia\nBye")

            voice("Hello"+z+"! I'm Tris your virtual assistant.")
            voice("I can open google for you, check the climate,time ,date, search wikipedia for information")

        elif "who are you" in query:
            playsound("bhasha.mp3")

        elif "excuse" in query:
            playsound("excus.mp3")

        elif "file reader" in query:
            nim=int(input(" Enter 1 for Reading Txt files \n Enter 2 for Reading Word files \n Enter 3 for Reading PDF's \n Your Choice :"))
            if nim ==1:
                file=input("Enter the file name :")
                f1 = open(file+'.txt')
                f=f1.read()
                voice("Opening the file sir!")
                print("Content : \n ",f)
                voice(f)    
            elif nim==2:
                file=input("Enter the file name :")
                f=wordre(file+'.docx')
                voice("Opening the file sir!")
                print("Content : \n ",f)
                voice(f)    
            elif nim==3:
                file=input("Enter the file name :")
                f=pdfre(file+'.pdf')
                voice("Opening the file sir!")
                print("Content : \n ",f)
                voice(f)    
            else:
                print("Enter a Valid Option!!!")


        elif "good word" in query:
            import random
            df=pd.read_csv("Thirukural.csv")
            df2=pd.read_csv("Thirukural With Explanation.csv")
            
            #replacing tabs with spaces to read clearly
            df['Verse']=df['Verse'].str.replace('\t',' ')
            # I dont see more difference between df and df_exp than an Explanation column.
            #Adding the Explanation column to df.
            df.loc[:,'Explanation']=df2.loc[:,'Explanation']
            df.reset_index()
                
            sv=random.randint(0,1329)
            result = df.loc[sv]
            tvoice(result["Verse"])
            #print("Kural        :",result["Verse"])
            print("Kural Number :",sv)
            print("Translation  :",result["Translation"])
            print("Meaning      :",result["Explanation"].split("Explanation :")[1])
            print("Paal         :",result["Chapter Name"])
            print("Adigaram     :",result["Section Name"])

        elif "child monitor" in query:
            word="abcdefghijklmnopqrstuvwxyz"
            sc=0
            for i in word:
                print("Say ",i,"...")
                voice(i)
                print("To Exit Say Break !")
                b=takeCommand()
                if b=="break":
                    break
                if i==b.lower():
                    print("Good!!!")
                    sc+=1
                else:
                    print("Try Again!!!")
            print("\nYour Score :",sc,'/26')

        elif "can we speak" in query:
            print("Sure "+z)
            voice("sure"+z)
            while True:
                print("Say something..")
                comm=takeCommand()

                if "wait" in comm:
                    print("Ok Sir!")
                    voice("Ok sir im going to sleep")
                    time.sleep(10)
                    voice("Back to your service sir")
                    continue
                
                if "hi" in comm:
                    print("Tris : Hello "+z)
                    voice("Hello "+z)
                    continue

                if "hello" in comm:
                    print("Tris : Hi "+z)
                    voice("Hi "+z)
                    continue

                elif "what to do" in comm:
                    print("Tris : go have dinner and sleep soon now "+z)
                    voice("go have dinner and sleep soon now "+z)
                    continue

                elif "money" in comm:
                     print("Tris : Yea....but I get lazy....and booking means I have to go to coimbatore to board....I don't wanna waste money.....🤓I am kind of very controlling in spending if not for food.....my father says I got it from my mom's family and mom says I got It from father family ")
                     voice("Yea....but I get lazy....and booking means I have to go to coimbatore to board....I don't wanna waste money.....🤓I am kind of very controlling in spending if not for food.....my father says I got it from my mom's family and mom says I got It from father family ")
                     continue
                    
                elif "say something" in comm:
                    print("Tris : Surya Clg: Sudharshan .......these guys are trolling with my name don't mind it okkkkii. I deeply  apologise  for her(aami)  pranks .....she is a little tooooo carefree and takes everything  silly"+z)
                    voice("Surya Clg : Sudharshan .......these guys are trolling with my name don't mind it okkkkii. I deeply  apologise  for her(aami)  pranks .....she is a little tooooo carefree and takes everything  silly "+z)
                    continue

                elif "how was the class" in comm:
                    print("Tris : Even I get u.....it was hard to cover up me yawning without a mask🥲✨"+z)
                    voice(" Even I get u.....it was hard to cover up me yawning without a mask🥲✨ "+z)
                    continue
                
                elif "get back" in comm:
                    print("Surya Clg : Alike in horror you might lose your favourite friend let's say anamika then in your remembrance she came to meet you at night. Already she is much like Annabelle. So think in ghost form. And founds that we planned her life so be a ghost and starts revemge. What so will be happen then. Will the great Surya survive or the Anamika drounch her blood thirst ? To be continued...")
                    voice("Surya Clg:Alike in horror you might lose your favourite friend let's say anamika then in your remembrance she came to meet you at night. Already she is much like Annabelle. So think in ghost form. And founds that we planned her life so be a ghost and starts revemge. What so will be happen then. Will the great Surya survive or the Anamika drounch her blood thirst ? To be continued...\nSurya Clg: i will die by laughing")
                    break
                elif "" in comm:
                    print("Say that again"+z)
                    voice("Say that again"+z)
                    continue
                response = chatbot.get_response(comm)
                print("Tris :",response)
                voice(response)

        elif "increase volume" in query:
            incv()
            voice("Increased volume")
        
        elif "decrease volume" in query:
            decv()
            voice("Decreased volume")

        elif "fortune time" in query:
            print("Fortune Teller!!!")
            print("Say the Event...")
            voice("Say The Event"+z)
            a=takeCommand()
            if a != " ":
                import random
                s=random.randint(1,8)
                if "marriage" in a:
                    playsound("orutha.mp3")
                    s=1
                if s==1:
                    print(a," will not happen in this lifetime!!!")
                    voice(a+" will not happen in this lifetime!!!")
                elif s==2:
                    print(a," will happen surely!!!")
                    voice(a+" will happen surely!!!")
                elif s==3:
                    print(a," will happen when you are 80 years!!!")
                    voice(a+" will happen when you are 80 years!!!")
                elif s==4:
                    print(a," may or may not happen!!!")
                    voice(a+" may or may not happen!!!")
                elif s==5:
                    print(a," will happen when you lose something which you like the most!!!")
                    voice(a+" will happen when you lose something which you like the most!!!")
                elif s==6:
                    print(a," can happen under gods grace!!!")
                    voice(a+" can happen under gods grace!!!")
                elif s==7:
                    print(a," will happen after a lot of struggle!!!")
                    voice(a+" will happen after a lot of struggle!!!")
                elif s==8:
                    print(a," will happen soon!!!")
                    voice(a+" will happen soon!!!")
                else:
                    print(a," will not happen!!!")
                    voice(a+" will not happen!!!")
            
            else:
                print("Please enter an event to check")
            time.sleep(3)
            print("Note: Future changes every second and this may or may not happen")

        elif "song time" in query:
            os.popen("spotify")
            time.sleep(5)
            pyautogui.hotkey('ctrl','l')
            time.sleep(2)
            voice("Say the song name "+z)
            song=takeCommand()
            pyautogui.write(song,interval=0.1)
            for key in ['enter','pagedown','tab','enter','enter']:
                time.sleep(2)
                pyautogui.press(key)
            pyautogui.press('enter')

        elif "wait" in query:
            print("Ok let me sleep then...")
            voice("Ok let me sleep then")
            time.sleep(10)
            voice("Back To your service "+z)

        elif "write" in query:
            print("Say what to write "+z)
            voice("Say what to write "+z)
            dfg=takeCommand()
            pyautogui.write(dfg)

        elif "press" in query:
            pyautogui.press('enter')

        elif "copy" in query:
            pyautogui.keyDown('ctrl')
            pyautogui.press('a')
            pyautogui.press('c')
            pyautogui.keyUp('ctrl')

        elif "cut" in query:
            pyautogui.keyDown('ctrl')
            pyautogui.press('a')
            pyautogui.press('x')
            pyautogui.keyUp('ctrl')

        elif "paste" in query:
            pyautogui.keyDown('ctrl')
            pyautogui.press('v')
            pyautogui.keyUp('ctrl')

        elif "save" in query:
            pyautogui.keyDown('ctrl')
            pyautogui.press('s')
            pyautogui.keyUp('ctrl')

        elif "click" in query:
            pyautogui.doubleClick()

        elif "scroll down" in query:
            pyautogui.scroll(-10)

        elif "scroll up" in query:
            pyautogui.scroll(10)

        elif "screenshot" in query:
            import pyscreenshot
            image = pyscreenshot.grab()
            image.show()
            #image.save("GeeksforGeeks.png")

        elif ("word" in query):
            pyttsx3.speak("Opening")
            pyttsx3.speak("MICROSOFT WORD")
            print(".")
            print(".")
            os.popen("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk")

        elif ("note" in query) or ("notes" in query) or ("notepad" in query) or ("editor" in query) or ("follow me" in query):
            pyttsx3.speak("Opening")
            pyttsx3.speak("NOTEPAD")
            print(".")
            print(".")
            os.popen("Notepad")
            
        elif "maximize" in query:
            Minimize = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(Minimize, win32con.SW_MAXIMIZE)

        elif "minimise" in query:
            Minimize = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
        elif "king game" in query:
            try:
                import rajarani.py
            except:
                print("Sorry exception came. No Worries as Sudharshan will repair me soon!!!")
                voice("Sorry exception came. No Worries as Sudharshan will repair me soon!!!")

        elif "number game" in query:
            try:
                #GUESSING NUMBERS
                import random
                x=random.randint(0,100)
                if x%2==0:
                    print("CLUE: The number is even!!!")
                else:
                    print("CLUE: The number is odd!!!")
                a=(x//10)
                b=(a+1)*10
                c=a*10
                print("The number is in range ",c,"and",b)
                ctr=0
                print("YOU HAVE 3 LIFES...")
                while ctr<3:
                    print()
                    y=int(input("Enter the number"))
                    if x==y:
                        print("You win!! :)")
                        print("The number is",x)
                        break
                    else:
                        ctr+=1
                        print("Its wrong!")
                        print("Try again")
                        print()
                if not ctr<3:
                    print("You lose :( \n The number is",x)
                    
            except:
                print("Sorry exception came. No Worries as Sudharshan will repair me soon!!!")
                voice("Sorry exception came. No Worries as Sudharshan will repair me soon!!!")

        elif "dice game" in query:
            try:
                import dice.py
            except:
                print("Sorry exception came. No Worries as Sudharshan will repair me soon!!!")
                voice("Sorry exception came. No Worries as Sudharshan will repair me soon!!!")

        else:
            voice("please pardon "+z)
            

Take_query()

