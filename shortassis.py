import pyttsx3;
import time;
import mysql.connector;
import speech_recognition as sr;
import os
import pprint
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
from bs4 import BeautifulSoup
import win32gui, win32con
import os
import math
import numpy as np
import pandas as pd 
import random
import pyautogui
import pywhatkit


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

voice("Welcome to Integrated virtual automated machine system")
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
for n1 in nam:
    for n2 in n1:
        print("Welcome back ",n2)
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
    greet="Itz Mid Night"+z
if g>=4 and g<7:
    print("Its Early Moring "+z+"!!!")
    greet="Its Early Moring"+z
if g>=7 and g<12:
    print("Good Morning "+z+"!!!")
    greet="Good Morning "+z
if g>=12 and g<16:
    print("Good Afternoon "+z+"!!")
    greet="Good Afternoon "+z
if g>=16 and g<20:
    print("Good Evening "+z+"!!!")
    greet="Good Evening "+z
if g>=20:
    print("Seems we are gonna have a wonderful night today "+z)
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

			# Number pf seconds of non-speaking audio before
			# a phrase is considered complete
			r.pause_threshold = 0.7
			audio = r.listen(source)

			# Voice input is identified
			try:

				# Listening voice commands in indian english
				print("Recognizing")
				Query = r.recognize_google(audio, language='en-in')

				# Displaying the voice command
				print("the query is printed='", Query, "'")

			except Exception as e:

				# Displaying exception
				print(e)
				# Handling exception
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
			print('Listening')

			# Number pf seconds of non-speaking audio before
			# a phrase is considered complete
			r.pause_threshold = 0.7
			audio = r.listen(source)

			# Voice input is identified
			try:

				# Listening voice commands in indian english
				print("Recognizing")
				Query = r.recognize_google(audio, language='en-in')

				# Displaying the voice command
				print("the query is printed='", Query, "'")

			except Exception as e:

				# Displaying exception
				print(e)
				# Handling exception
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
        mytext = str(translation.text)
        pyttsx3.speak(mytext)
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

        elif "translate" in query:
            sharini()

        elif "close" in query and"tata" in query:
            voice("Bye. Have a great day"+z)
            print("Shut down initiating...")
            Maam = Gfg()
            Maam.quitSelf()
            
        elif "restart system" in query:
            voice("Bye. Have a great day"+z)
            print("Restart initiating...")
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
            
            print("\n\t 1.MICROSOFT WORD \t 2.MICROSOFT POWERPOINT \n\t 3.MICROSOFT EXCEL \t 4.CALCULATOR \n\t 5.ANDROID STUDIO\t 6.VS CODE \n\t 7.WAMP SERVER \t \t 8.MICROSOFT EDGE \n\t 9.NOTEPAD	 \t 10.ORACLE VBOX \n\n\t\t	 0. FOR EXIT TOOLS")
            
            print("\n	 (YOU CAN USE NUMBER OR YOU CAN DO CHAT LIKE 'OPEN NOTEBOOK' etc....)")
            
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
            voice("Hello"+z+"! I'm Tris your virtual assistant.")

        elif "good word" in query:

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
            voice("Kural        :"+result["Verse"])
            print("Kural        :",result["Verse"])
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
                b=takeCommand()
                if i==b.lower():
                    print("Good!!!")
                    sc+=1
                else:
                    print("Try Again!!!")
            print("\nYour Score :",sc,'/26')

        elif "fortune time" in query:
            print("Fortune Teller!!!")
            print("Say the Event...")
            voice("Say The Event"+z)
            a=takeCommand()
            if a != " ":
                import random
                s=random.randint(1,8)
                
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

        elif "maximize" in query:
            Minimize = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(Minimize, win32con.SW_MAXIMIZE)

        elif "minimise" in query:
            Minimize = win32gui.GetForegroundWindow()
            win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
        elif "king game" in query:
            import rajarani.py

        else:
            voice("please pardon "+z)
            

Take_query()






